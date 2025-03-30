from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from bson.objectid import ObjectId  

db = settings.DATABASE
books_collection = db["books"]
authors_collection = db["authors"]

@csrf_exempt
def create_book(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            required_fields = ["isbn", "title", "description", "price", "author","author_id", "genre", "publisher", "published_year", "rating"]
            for field in required_fields:
                if field not in data:
                    return JsonResponse({"error": f"Missing field: {field}"}, status=400)

            result = books_collection.insert_one(data)
            return JsonResponse({"message": "Book created successfully", "id": str(result.inserted_id)}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

def get_book_by_isbn(request, isbn):
    if request.method == "GET":
        book = books_collection.find_one({"isbn": isbn}, {"_id": 0})
        if book:
            return JsonResponse(book, status=200)
        else:
            return JsonResponse({"error": "Book not found"}, status=404)

@csrf_exempt
def create_author(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            required_fields = ["first_name", "last_name", "biography", "publisher", "author_id"]
            for field in required_fields:
                if field not in data:
                    return JsonResponse({"error": f"Missing field: {field}"}, status=400)

            result = authors_collection.insert_one(data)
            return JsonResponse({"message": "Author created successfully", "id": str(result.inserted_id)}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

def get_books_by_author(request, author_id):
    if request.method == "GET":
        books = list(books_collection.find({"author_id": author_id}, {"_id": 0}))
        return JsonResponse(books, safe=False)

@csrf_exempt
def update_book(request, book_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            result = books_collection.update_one({"_id": ObjectId(book_id)}, {"$set": data})
            if result.modified_count:
                return JsonResponse({"message": "Book updated successfully"})
            return JsonResponse({"message": "No changes made"}, status=304)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def delete_book(request, book_id):
    if request.method == "DELETE":
        try:
            result = books_collection.delete_one({"_id": ObjectId(book_id)})
            if result.deleted_count:
                return JsonResponse({"message": "Book deleted successfully"})
            return JsonResponse({"error": "Book not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)