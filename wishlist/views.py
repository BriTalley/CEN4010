import json
from bson import ObjectId
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Wishlist, Book, ShoppingCart

@csrf_exempt
def create_wishlist(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            name = data.get('name')
            if not user_id or not name:
                return HttpResponseBadRequest("Missing 'user_id' or 'name' parameter.")
            Wishlist.objects.create(user_id=user_id, name=name)
            return HttpResponse(status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Invalid HTTP method. Use POST.")

@csrf_exempt
def add_book_to_wishlist(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            wishlist_id = data.get('wishlist_id')
            isbn = data.get('isbn')
            if not wishlist_id or not isbn:
                return HttpResponseBadRequest("Missing wishlist_id or isbn")
            try:
                wishlist = Wishlist.objects.get(id=ObjectId(wishlist_id))
            except Wishlist.DoesNotExist:
                return JsonResponse({'error': 'Wishlist not found'}, status=404)
            try:
                book = Book.objects.get(isbn=str(isbn))
            except Book.DoesNotExist:
                return JsonResponse({'error': 'Book not found'}, status=404)
            wishlist.books.add(book)
            return HttpResponse(status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Invalid HTTP method. Use POST.")

@csrf_exempt
def remove_book_from_wishlist_to_cart(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            wishlist_id = data.get('wishlist_id')
            isbn = data.get('isbn')
            if not wishlist_id or not isbn:
                return HttpResponseBadRequest("Missing wishlist_id or isbn")
            try:
                wishlist = Wishlist.objects.get(id=ObjectId(wishlist_id))
            except Wishlist.DoesNotExist:
                return JsonResponse({'error': 'Wishlist not found'}, status=404)
            try:
                book = Book.objects.get(isbn=str(isbn))
            except Book.DoesNotExist:
                return JsonResponse({'error': 'Book not found'}, status=404)
            wishlist.books.remove(book)
            cart, created = ShoppingCart.objects.get_or_create(user_id=wishlist.user_id)
            cart.books.add(book)
            return HttpResponse(status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Invalid HTTP method. Use DELETE.")

def list_wishlist_books(request, wishlist_id):
    if request.method == 'GET':
        try:
            wishlist = Wishlist.objects.get(id=ObjectId(wishlist_id))
        except Wishlist.DoesNotExist:
            return JsonResponse({'error': 'Wishlist not found'}, status=404)
        books_data = []
        for book in wishlist.books.all():
            books_data.append({
                "isbn": book.isbn,
                "title": book.title,
                "author": book.author,
                "genre": book.genre,
                "published_year": book.published_year,
                "rating": book.rating,
                "price": book.price,
                "copies_sold": book.copies_sold,
            })
        response_data = {
            "wishlist_id": str(wishlist.id),
            "wishlist_name": wishlist.name,
            "user_id": wishlist.user_id,
            "books": books_data
        }
        return JsonResponse(response_data, status=200)
    else:
        return HttpResponseBadRequest("Invalid HTTP method. Use GET.")
