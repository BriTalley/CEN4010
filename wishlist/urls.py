from django.urls import path
from . import views

urlpatterns = [
    # Part 1: Create a Wishlist
    path('wishlist/create/', views.create_wishlist, name='create_wishlist'),
    # Part 2: Add a Book to a Wishlist (and return wishlist details)
    path('wishlist/add/', views.add_book_to_wishlist, name='add_book_to_wishlist'),
    # Part 3: Move a Book from Wishlist to Shopping Cart
    path('wishlist/move_to_cart/', views.move_book_from_wishlist_to_cart, name='move_book_from_wishlist_to_cart'),
     # Part 4: List Books in a Wishlist
    path('wishlist/<str:wishlist_id>/books/', views.list_wishlist_books, name='list_wishlist_books'),
]
