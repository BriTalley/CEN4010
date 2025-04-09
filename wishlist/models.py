from djongo import models
from bson import ObjectId

class Book(models.Model):
    isbn = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    published_year = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    copies_sold = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "books"
        managed = False

class Wishlist(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False, db_column='_id')
    name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, blank=True)

    class Meta:
        unique_together = ('user_id', 'name')

    def __str__(self):
        return f"{self.name} (User: {self.user_id})"

class ShoppingCart(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False, db_column='_id')
    user_id = models.CharField(max_length=255, unique=True)
    books = models.ManyToManyField(Book, blank=True)

    class Meta:
        db_table = "shopping_cart"

    def __str__(self):
        return f"Shopping Cart for {self.user_id}"
