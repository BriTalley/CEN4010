from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['username', 'password', 'name', 'email', 'home_address']

    def create(self, validated_data):
        return users.objects.create(**validated_data)

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'