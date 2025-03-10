from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import users
from .serializers import UserSerializer

@api_view(['POST'])
def create_user(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    user = users.objects.create(
        username=username,
        password=password,  
        name=data.get('name', ''),
        email=data.get('email', ''),
        home_address=data.get('home_address', '')
    )

    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)