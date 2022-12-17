from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from CarDealerShip.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from CarDealerShip.photos.models import Photos
from CarDealerShip.wishlist.forms import PhotoCommentForm
from CarDealerShip.wishlist.models import PhotoComment


def details_photo(request, pk):
    photo = Photos.objects.filter(pk=pk) \
        .get()

    user_wish_photos = Photos.objects.filter(pk=pk, user_id=request.user.pk)

    context = {
        'photo': photo,
        'has_user_wish_photo': user_wish_photos,
        'is_owner': request.user == photo.user,
        'comments': PhotoComment.objects.all(),
        'comment_form': PhotoCommentForm(),
    }

    return render(
        request,
        'photos/photo-details-page.html',
        context,
    )


def get_post_photo_form(request, form, success_url, template_path, pk=None):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(success_url)

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, template_path, context)


@login_required
def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()

            return redirect('details photo', pk=photo.pk)

    context = {
        'form': form,
    }

    return render(
        request,
        'photos/photo-add-page.html',
        context,
    )


@login_required
def edit_photo(request, pk):
    photo = Photos.objects.filter(pk=pk) \
        .get()
    return get_post_photo_form(
        request,
        PhotoEditForm(request.POST or None, instance=photo),
        success_url=reverse('posts'),
        template_path='photos/photo-edit-page.html',
        pk=pk,
    )


@login_required
def delete_photo(request, pk):
    photo = Photos.objects.filter(pk=pk) \
        .get()
    return get_post_photo_form(
        request,
        PhotoDeleteForm(request.POST or None, instance=photo),
        success_url=reverse('posts'),
        template_path='photos/photo-delete-page.html',
        pk=pk,
    )
