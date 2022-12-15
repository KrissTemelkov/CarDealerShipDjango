from django.urls import path, include

from CarDealerShip.common.views import index, catalogue, car_edit, car_create, car_delete,\
    car_details

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('car/', include([
        path('create/', car_create, name='car create'),
        path('<int:pk>/details/', car_details, name='car details'),
        path('<int:pk>/edit', car_edit, name='car edit'),
        path('<int:pk>/delete/', car_delete, name='car delete'),
    ]))
)
