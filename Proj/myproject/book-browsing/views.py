from django.shortcuts import render

# Create your views here.

# books/views.py
import json
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.http import require_http_methods
from pymongo import MongoClient
from bson import json_util

# Initialize MongoDB client (this will run once when the module is imported)
client = MongoClient(settings.MONGODB_CONNECTION_STRING)
db = client[settings.MONGODB_DB_NAME]
books_collection = db['books']  # Ensure this matches your MongoDB collection name

@require_http_methods(["GET"])
def books_by_genre(request):
    # Get the 'genre' parameter from the query string
    genre = request.GET.get('genre')
    if not genre:
        return JsonResponse({'error': 'Genre parameter is required'}, status=400)
    
    # Query the MongoDB collection for books with the specified genre
    books_cursor = books_collection.find({'genre': genre})
    books_list = list(books_cursor)
    
    
    # Convert BSON data (e.g., ObjectId) into JSON serializable format
    books_json = json.loads(json_util.dumps(books_list))
    
    return JsonResponse(books_json, safe=False)

def books_by_rating(request):

    rating_input = request.GET.get('rating')
    if not rating_input:
        return JsonResponse({'error': 'rating parameter is required'}, status=400)
        
    # Query all books in the collection
    threshold = float(rating_input)
    books_cursor = books_collection.find({'rating': {'$gte': threshold}})
    books_list = list(books_cursor)
    
    # Convert BSON data (e.g., ObjectId) into JSON serializable format
    books_json = json.loads(json_util.dumps(books_list))
    
    # Organize books by their ratings
    organized_books = {}
    for book in books_json:
        # Use 'Unknown' as default if the rating field is missing
        rating = book.get('rating', 'Unknown')
        organized_books.setdefault(rating, []).append(book)

        def rating_key(r):
            try:
                return float(r)
            except (ValueError, TypeError):
                return float('-inf')

        # Sort the ratings in descending order (highest first)
    sorted_ratings = sorted(organized_books.keys(), key=lambda r: rating_key(r), reverse=True)
    
    # Build an ordered dictionary with the sorted keys
    ordered_books = {rating: organized_books[rating] for rating in sorted_ratings}
    
    return JsonResponse(ordered_books, safe=False)

def top_ten_books(request):
    # Query top 10 books by 'copies_sold' in descending order
    books_cursor = books_collection.find({}).sort("copies_sold", -1).limit(10)
    books_list = list(books_cursor)
    
    # Convert BSON data into JSON serializable format
    books_json = json.loads(json_util.dumps(books_list))
    
    # Return the data wrapped in a "top_books" key
    return JsonResponse({"top_books": books_json}, safe=False)


def all_books(request):
    # Retrieve all documents without filtering
    books_cursor = books_collection.find()
    books_list = list(books_cursor)
    
    # Convert BSON to JSON-serializable format
    books_json = json.loads(json_util.dumps(books_list))
    
    return JsonResponse(books_json, safe=False)