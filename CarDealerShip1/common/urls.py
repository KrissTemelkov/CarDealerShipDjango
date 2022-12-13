from django.urls import path

from CarDealerShip1.common.views import index

urlpatterns = (
    path('', index, name='index'),

)
