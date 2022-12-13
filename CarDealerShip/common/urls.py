from django.urls import path

from CarDealerShip.common.views import index

urlpatterns = (
    path('', index, name='index'),

)
