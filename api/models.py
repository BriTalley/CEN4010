from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

class users(models.Model):
    # Required Fields
    username = models.CharField(
        max_length=15, 
        unique=True, 
        validators=[MinLengthValidator(5)]
    )
    password = models.CharField(
        max_length=30, 
        validators=[MinLengthValidator(8)]
    )
    
    # Optional Fields
    name = models.CharField(max_length= 255, blank=True, null=True)
    email = models.CharField(max_length = 255, blank=True, null = True)
    home_address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username

class CreditCard(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    card_number = models.CharField(
        max_length=16,
        validators=[MinLengthValidator(16)]
    )
    card_holder = models.CharField(max_length=100)
    expiration_date = models.CharField(
        max_length=5,
        validators=[MinLengthValidator(3)]
    )
    cvv = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)]
    )

    def __str__(self):
           return f"{self.card_holder} - {self.card_number[-4:]}"

      