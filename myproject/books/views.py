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

def all_books(request):
    # Retrieve all documents without filtering
    books_cursor = books_collection.find()
    books_list = list(books_cursor)
    
    # Convert BSON to JSON-serializable format
    books_json = json.loads(json_util.dumps(books_list))
    
    return JsonResponse(books_json, safe=False)