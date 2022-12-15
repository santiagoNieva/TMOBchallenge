from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_GET
from .models import Redirect
# Create your views here.

@require_GET
def get_url(request):
    key = request.GET.get('key',None)
    if not key:
        return JsonResponse({'error': 'You missed the key parameter.'}, status=400)
        
    url = Redirect.get_redirect(key)

    if url:
        return JsonResponse({'key':key,'url':url},status=200)
    else:
        return JsonResponse({'error': 'The provided key does not exist'}, status=404)    
    