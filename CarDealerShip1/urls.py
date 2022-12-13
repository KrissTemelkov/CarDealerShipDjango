from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('CarDealerShip1.accounts.urls')),
    path('', include('CarDealerShip1.common.urls')),

]


