from django.core.validators import MinLengthValidator
from django.db import models
from djongo import models
import uuid

# Create your models here.
class users(models.Model):
    _id = models.ObjectIdField(default=uuid.uuid4, unique=True) #custom field
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
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    home_address = models.CharField(max_length=255, null=True, blank=True)

def __str__(self):
    return self.username