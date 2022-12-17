from django.contrib import admin

from CarDealerShip.common.forms import CarEditForm, CarCreateForm
from CarDealerShip.common.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    form = CarEditForm
    add_form = CarCreateForm
