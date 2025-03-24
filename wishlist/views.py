import json
from bson import ObjectId
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Wishlist, Book, ShoppingCart

# Part 1: Create a Wishlist
@csrf_exempt
def create_wishlist(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            name = data.get('name')
            if not user_id or not name:
                return HttpResponseBadRequest("Missing 'user_id' or 'name' parameter.")
            wishlist = Wishlist.objects.create(user_id=user_id, name=name)
            # Return the wishlist id (as a string) in the response.
            return JsonResponse({'wishlist_id': str(wishlist.id)}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Invalid HTTP method. Use POST.")

# Part 2: Add a Book to a Wishlist and Return Wishlist Details
@csrf_exempt
def add_book_to_wishlist(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            wishlist_id = data.get('wishlist_id')
            book_id = data.get('book_id')  # Expecting a string like "9780439136365"
            if not wishlist_id or not book_id:
                return HttpResponseBadRequest("Missing wishlist_id or book_id")
            try:
                # Convert wishlist_id to an ObjectId
                wishlist = Wishlist.objects.get(id=ObjectId(wishlist_id))
            except Wishlist.DoesNotExist:
                return JsonResponse({'error': 'Wishlist not found'}, status=404)
            try:
                # Look up the book using the numeric identifier stored as a string.
                book = Book.objects.get(book_id=str(book_id))
            except Book.DoesNotExist:
                return JsonResponse({'error': 'Book not found'}, status=404)
            # Add the book to the wishlist.
            wishlist.books.add(book)
            # Now retrieve the wishlist with all its books.
            wishlist = Wishlist.objects.get(id=ObjectId(wishlist_id))
            books_data = []
            for b in wishlist.books.all():
                books_data.append({
                    "book_id": b.book_id,
                    "title": b.title,
                })
            response_data = {
                "wishlist_name": wishlist.name,
                "user_id": wishlist.user_id,
                "books": books_data
            }
            return JsonResponse(response_data, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Invalid HTTP method. Use POST.")
    
@csrf_exempt
def move_book_from_wishlist_to_cart(request):
    """
    Part 3:
    DELETE request that removes a book from a wishlist and adds it to the user's shopping cart.
    Expected JSON body: { "wishlist_id": "...", "book_id": "..." }
    """
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            wishlist_id = data.get('wishlist_id')
            book_id = data.get('book_id')  # Expecting a string (e.g., "9780439136365")
            if not wishlist_id or not book_id:
                return HttpResponseBadRequest("Missing wishlist_id or book_id")
            
            # Retrieve the wishlist by converting the string id to an ObjectId.
            try:
                wishlist = Wishlist.objects.get(id=ObjectId(wishlist_id))
            except Wishlist.DoesNotExist:
                return JsonResponse({'error': 'Wishlist not found'}, status=404)
            
            # Look up the book in the shared books collection.
            try:
                book = Book.objects.get(book_id=str(book_id))
            except Book.DoesNotExist:
                return JsonResponse({'error': 'Book not found'}, status=404)
            
            # Remove the book from the wishlist.
            wishlist.books.remove(book)
            
            # Get the user_id from the wishlist.
            user_id = wishlist.user_id
            
            # Retrieve the shopping cart for the user, or create one if it doesn't exist.
            shopping_cart, created = ShoppingCart.objects.get_or_create(user_id=user_id)
            
            # Add the book to the shopping cart.
            shopping_cart.books.add(book)
            
            # Return a 204 No Content status (or 200 OK if you prefer).
            return HttpResponse(status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Invalid HTTP method. Use DELETE.")
    
def list_wishlist_books(request, wishlist_id):
    """
    Part 4: List the books in a user's wishlist.
    HTTP Method: GET
    URL Parameter: wishlist_id (string)
    Response: JSON containing wishlist info and an array of book details.
    """
    if request.method == 'GET':
        try:
            # Convert the wishlist_id string to an ObjectId and fetch the wishlist.
            wishlist = Wishlist.objects.get(id=ObjectId(wishlist_id))
        except Wishlist.DoesNotExist:
            return JsonResponse({'error': 'Wishlist not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
        # Build a list of book details from the many-to-many relationship.
        books_data = []
        for book in wishlist.books.all():
            books_data.append({
                "book_id": book.book_id,
                "title": book.title,
            })
        
        # Prepare the response data.
        response_data = {
            "wishlist_id": str(wishlist.id),
            "wishlist_name": wishlist.name,
            "user_id": wishlist.user_id,
            "books": books_data
        }
        return JsonResponse(response_data, status=200)
    else:
        return HttpResponseBadRequest("Invalid HTTP method. Use GET.")
