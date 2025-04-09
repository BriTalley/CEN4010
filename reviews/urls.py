from django.urls import path
from .views import add_review, get_reviews

urlpatterns = [
    path("add/", add_review, name="add_review"),  # URL for adding a review
    path("<str:book_id>/", get_reviews, name="get_reviews"),  # URL for fetching reviews
]
