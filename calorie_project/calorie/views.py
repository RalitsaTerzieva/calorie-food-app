from django.shortcuts import render
from .models import Food, Consume

def index(request):
    if request.method == 'POST':
        consumed_food = request.POST['consumed_food']
        consume = Food.objects.get(name=consumed_food)
        user = request.user
        consume = Consume(user=user,consumed_food=consume)
        consume.save()
        foods = Food.objects.all()
    else:
        foods = Food.objects.all()
    return render(request, 'food/index.html', {'foods': foods})

