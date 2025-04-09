from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/create/', views.create_wishlist, name='create_wishlist'),
    path('wishlist/add/', views.add_book_to_wishlist, name='add_book_to_wishlist'),
    path('wishlist/move_to_cart/', views.remove_book_from_wishlist_to_cart, name='remove_book_from_wishlist_to_cart'),
    path('wishlist/<str:wishlist_id>/books/', views.list_wishlist_books, name='list_wishlist_books'),
]
