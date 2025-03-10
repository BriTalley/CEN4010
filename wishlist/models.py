from django.db import models
# Create your models here.
class Wishlist(models.Model):
    name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)

    class Meta:
        unique_together = ('user_id', 'name')

    def __str__(self):
        return f"{self.name} (User: {self.user_id})"
