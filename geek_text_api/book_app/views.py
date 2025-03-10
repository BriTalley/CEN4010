from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from bson.objectid import ObjectId  

db = settings.DATABASE
collection = db["books"]

@csrf_exempt
def create_book(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            result = collection.insert_one(data)
            return JsonResponse({"message": "Book created successfully", "id": str(result.inserted_id)}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

def get_books(request):
    if request.method == "GET":
        books = list(collection.find({}, {"_id": 0}))  # Excluding _id from response
        return JsonResponse({"books": books}, safe=False)

@csrf_exempt
def update_book(request, book_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            result = collection.update_one({"_id": ObjectId(book_id)}, {"$set": data})
            if result.modified_count:
                return JsonResponse({"message": "Book updated successfully"})
            return JsonResponse({"message": "No changes made"}, status=304)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def delete_book(request, book_id):
    if request.method == "DELETE":
        try:
            result = collection.delete_one({"_id": ObjectId(book_id)})
            if result.deleted_count:
                return JsonResponse({"message": "Book deleted successfully"})
            return JsonResponse({"error": "Book not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
