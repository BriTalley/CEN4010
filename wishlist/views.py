import json
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Wishlist

@csrf_exempt
def create_wishlist(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body.
            data = json.loads(request.body)
            user_id = data.get('user_id')
            name = data.get('name')
            
            # Error for bad request.
            if not user_id or not name:
                return HttpResponseBadRequest("Missing 'user_id' or 'name' parameter.")
            
            # Create the wishlist.
            Wishlist.objects.create(user_id=user_id, name=name)
            
            # Return a 201 Created response.
            return HttpResponse(status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Invalid HTTP method. Use POST.")
