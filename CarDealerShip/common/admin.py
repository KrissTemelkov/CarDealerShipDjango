from django.contrib import admin

from CarDealerShip.common.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
