from django.urls import path

from CarDealerShip.accounts.views import profile_info

urlpatterns = (
    path('', profile_info, name='accountInfo'),
)
