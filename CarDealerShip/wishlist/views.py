
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from CarDealerShip.wishlist.utils import get_photo_url
from CarDealerShip.wishlist.forms import PhotoCommentForm, SearchPhotosForm
from CarDealerShip.wishlist.models import PhotoWish, PhotoComment

from CarDealerShip.photos.models import Photos


def posts(request):
    search_form = SearchPhotosForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['car_name']

    photos = Photos.objects.all()

    if search_pattern:
        photos = photos.filter(tagged_cars__name__icontains=search_pattern)

    context = {
        'photos': photos,
        'comments': PhotoComment.objects.all(),
        'comment_form': PhotoCommentForm(),
        'search_form': search_form,
    }
    # for wish in PhotoWish.objects.all():
    #     if photo.pk == wish.photo and wish.user == request.user.pk:
    #         photo['wished'] = True
    #     else:
    #         pass
    #         # photo['wished'] = False

    return render(
        request,
        'photos/posts-page.html',
        context,
    )


@login_required
def wish_photo(request, photo_id):
    user_wish_photos = PhotoWish.objects \
        .filter(photo_id=photo_id, user_id=request.user.pk)

    if user_wish_photos:
        user_wish_photos.delete()
    else:
        PhotoWish.objects.create(
            photo_id=photo_id,
            user_id=request.user.pk,
        )

    return redirect(get_photo_url(request, photo_id))


@login_required
def comment_photo(request, photo_id):
    photo = Photos.objects.filter(pk=photo_id) \
        .get()

    form = PhotoCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.photo = photo
        comment.save()

    return redirect('posts')
