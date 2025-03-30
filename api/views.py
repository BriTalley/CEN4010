from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import users
from .serializers import UserSerializer

@api_view(['GET'])
def home_page(request):
    if request.method == 'GET':
        return Response({'This is the user creation API for Geek Text!'})

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
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

        return Response({'User created successfully'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_user(request, username):
    try:
        user = users.objects.get(username = username)
    except users.DoesNotExist:
        return Response ({'error: Username not found'}, status = status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

    
#@api_view(['PUT'])


#@api_view(['POST'])
