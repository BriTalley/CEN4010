from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import users
from .serializers import UserSerializer

# Create your views here.
class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)