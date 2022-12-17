from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from CarDealerShip.common.forms import CarCreateForm, CarEditForm, CarDeleteForm
from CarDealerShip.common.models import Car


def index(request):
    return render(request, 'common/index.html')


def catalogue(request):
    loged = request.user.is_authenticated
    if not loged:
        return redirect('index')
    cars = Car.objects.all()
    cars = cars.filter(user_id=request.user.pk)

    context = {
        'size': len(cars),
        'cars': cars,
    }
    return render(request, 'common/catalogue.html', context)


@login_required
def car_create(request):
    if request.method == 'GET':
        form = CarCreateForm
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'common/car-create.html', context)


def car_details(request, pk):
    car = Car.objects.filter(pk=pk)\
        .get()
    context = {
        "car": car
    }
    return render(request, 'common/car-details.html', context)


@login_required
def car_edit(request, pk):
    car = Car.objects.filter(pk=pk)\
        .get()
    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'car': car
    }
    return render(request, 'common/car-edit.html', context)


@login_required
def car_delete(request, pk):
    car = Car.objects.filter(pk=pk) \
        .get()
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'car': car
    }
    return render(request, 'common/car-delete.html', context)

