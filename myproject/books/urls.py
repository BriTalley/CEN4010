# books/urls.py
from django.urls import path
from .views import books_by_genre,all_books

urlpatterns = [
    path('books/', books_by_genre, name='books_by_genre'),
    path('all-books/', all_books, name='all_books'),
]
