from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Review  # Ensure you have your Review model imported

@csrf_exempt  # This disables CSRF protection for this function
def add_review(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            new_review = Review.objects.create(
                book_id=data["book_id"],
                username=data["username"],
                rating=data["rating"],
                comment=data["comment"]
            )
            return JsonResponse({"message": "Review added!", "review_id": new_review.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

def get_reviews(request, book_id):
    if request.method == "GET":
        reviews = Review.objects.filter(book_id=book_id)
        reviews_list = list(reviews.values())
        return JsonResponse(reviews_list, safe=False)

