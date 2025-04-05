from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import users
from .serializers import *

@api_view(['GET'])
def home_page(request):
    return Response({'This is the user creation API for Geek Text!'})

@api_view(['POST'])
def create_user(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required'})
    
    user = users.objects.create(
        username=username,
        password=password,  
        name=data.get('name', ''),
        email=data.get('email', ''),
        home_address=data.get('home_address', '')
    )

    return Response({'User created successfully'})


@api_view(['GET'])
def get_user(request, username):
    try:
        user = users.objects.get(username = username)
    except users.DoesNotExist:
        return Response ({'error: Username not found'})
    
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

    
@api_view(['PUT'])
def update_user(request, username):
    try:
        user = users.objects.get(username = username)
    except users.DoesNotExist:
        return Response ({'error: Username not found'})
    
    if 'email' in request.data:
        return Response ({'error: Email cannot be changed'})
    
    serializer = UserSerializer(user, data = request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response ({'User updated successfully!'})

    return Response({'Could not update user. Please try again.'})
    



@api_view(['POST'])
def create_credit_card(request, username):
    try:
        user = users.objects.get(username = username)
    except:
        return Response({'User not found.'})
    
    data = request.data.copy()
    request.data['user'] = user.id
    
    serializer = CreditCardSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Credit Card saved successfully!'})
    return Response({'Credit Card could not be saved. Please ensure details are correct and try again.'})
