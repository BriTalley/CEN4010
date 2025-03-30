from djongo import models

class Review(models.Model):
    book_id = models.CharField(max_length=255)  # Reference to the book
    username = models.CharField(max_length=100)  # Who left the review
    rating = models.IntegerField()  # Rating from 1-5
    comment = models.TextField()  # Review comment
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return f"{self.username} - {self.rating}/5"


