from django.urls import path
from .views import *
from .models import users

urlpatterns = [
    path('', home_page, name = 'home-page'),
    path('create-user/', create_user, name='create-user'),
    path('get-user/<str:username>/', get_user, name='get-user'),
]