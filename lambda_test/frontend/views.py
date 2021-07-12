from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
  return JsonResponse({
    'confirmation': 'success'
  })

def home(request):
  return render(request, 'frontend/index.html', {
    'greeting': 'test!'
  })