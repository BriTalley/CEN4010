from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.create_book), 
    path('books/<str:isbn>/', views.get_book_by_isbn), 
    path('authors/', views.create_author),  
    path('authors/<str:author_id>/books/', views.get_books_by_author),
    path('books/update/<str:book_id>/', views.update_book),
    path('books/delete/<str:book_id>/', views.delete_book), 
]
