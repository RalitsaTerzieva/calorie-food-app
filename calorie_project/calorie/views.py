from django.shortcuts import render
from .models import Food

def index(request):
    foods = Food.objects.all()
    return render(request, 'food/index.html', {'foods': foods})

