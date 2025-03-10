from django.urls import path
from . import views

urlpatterns = [
    # The endpoint to create a wishlist.
    path('wishlist/create/', views.create_wishlist, name='create_wishlist'),
]
