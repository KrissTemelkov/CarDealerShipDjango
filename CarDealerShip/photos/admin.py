from django.contrib import admin

from CarDealerShip.photos.models import Photos


@admin.register(Photos)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date', 'cars')

    @staticmethod
    def cars(current_photo_obj):
        tagged_cars = current_photo_obj.tagged_cars.all()
        if tagged_cars:
            return ', '.join(p.name for p in tagged_cars)
        return 'No cars'
