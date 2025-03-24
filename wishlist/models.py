from djongo import models
from bson import ObjectId


class Book(models.Model):
    # We assume book_id is stored as a string (e.g., "9780439136365") in the shared collection.
    book_id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "books"   # Use the existing shared collection.
        managed = False      # Mark as unmanaged so Django doesn't alter the schema.

class Wishlist(models.Model):
    # Use ObjectIdField stored in MongoDB's _id field.
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False, db_column='_id')
    name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, blank=True)

    class Meta:
        unique_together = ('user_id', 'name')

    def __str__(self):
        return f"{self.name} (User: {self.user_id})"
    
class ShoppingCart(models.Model):
    # Each shopping cart is associated with one user.
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False, db_column='_id')
    user_id = models.CharField(max_length=255, unique=True)
    books = models.ManyToManyField(Book, blank=True)

    class Meta:
        db_table = "shopping_cart"

    def __str__(self):
        return f"Shopping Cart for {self.user_id}"
