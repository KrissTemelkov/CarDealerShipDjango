from django.contrib import admin

from CarDealerShip.wishlist.models import PhotoComment


@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    pass
