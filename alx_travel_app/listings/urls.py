from django.urls import path
from django.http import JsonResponse

def test_view(request):
    return JsonResponse({'message': 'Hello from Listings API'})

urlpatterns = [
    path('test/', test_view),
]
