book_reviews
# CEN4010
 ## Book Reviews and Commenting API

### POST /reviews/add/
Adds a new review to the database.

Required JSON fields:
- book_id (string)
- username (string)
- rating (integer from 1 to 5)
- comment (text)

Example JSON:
{
  "book_id": "456",
  "username": "cvd_demo",
  "rating": 4,
  "comment": "Solid read with great pacing."
}



### GET /reviews/<book_id>/
Returns all reviews for a specific book ID.

Example URL:  
http://127.0.0.1:8000/reviews/456/

Expected Response:
[
  {
    "id": 1,
    "book_id": "456",
    "username": "cvd_demo",
    "rating": 4,
    "comment": "Solid read with great pacing.",
    "created_at": "2025-03-24T23:59:49.789Z"
 

CEN 4010 - Group 10
main
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Review

@csrf_exempt
def update_review(request, review_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            review = Review.objects.get(id=review_id)

            review.rating = data.get("rating", review.rating)
            review.comment = data.get("comment", review.comment)
            review.save()

            return JsonResponse({"message": "Review updated!"})
        except Review.DoesNotExist:
            return JsonResponse({"error": "Review not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
def delete_review(request, review_id):
    if request.method == "DELETE":
        try:
            review = Review.objects.get(id=review_id)
            review.delete()
            return JsonResponse({"message": "Review deleted!"})
        except Review.DoesNotExist:
            return JsonResponse({"error": "Review not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)
### PUT /reviews/update/<review_id>/
Updates a review’s rating or comment using the review ID.

Example JSON body:
{
  "rating": 5,
  "comment": "Updated comment text here."
}

---

### DELETE /reviews/delete/<review_id>/
Deletes a review by its review ID.

Expected Response:
{
  "message": "Review deleted!"
}
