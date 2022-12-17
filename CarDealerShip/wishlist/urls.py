from django.urls import path

from CarDealerShip.wishlist.views import wish_photo, comment_photo, posts

urlpatterns = (
    path('', posts, name='posts'),
    path('wish/<int:photo_id>/', wish_photo, name='wish photo'),
    path('comment/<int:photo_id>/', comment_photo, name='comment photo'),
)
