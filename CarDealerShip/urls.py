from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('CarDealerShip.accounts.urls')),
    path('photos/', include('CarDealerShip.photos.urls')),
    path('posts/', include('CarDealerShip.wishlist.urls')),
    path('', include('CarDealerShip.common.urls')),

]


