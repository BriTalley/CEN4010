# books/urls.py
from django.urls import path
from .views import books_by_genre,all_books,books_by_rating,top_ten_books

urlpatterns = [
    path('genre-books/', books_by_genre, name='books_by_genre'),
    path('all-books/', all_books, name='all_books'),
    path('rating-books/', books_by_rating, name='books_by_rating'),
    path('top-ten-books/', top_ten_books, name='top_ten')
]
