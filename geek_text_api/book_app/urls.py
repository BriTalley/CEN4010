from django.urls import path
from .views import create_book, get_books, update_book, delete_book

urlpatterns = [
    path("books/", get_books, name="get_books"),
    path("books/create/", create_book, name="create_book"),
    path("books/update/<str:book_id>/", update_book, name="update_book"),
    path("books/delete/<str:book_id>/", delete_book, name="delete_book"),
]
