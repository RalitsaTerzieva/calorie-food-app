from django.shortcuts import render
from .models import Food, Consume

def index(request):
    if request.method == 'POST':
        consumed_food = request.POST['food_consumed']
        consume = Food.objects.get(name=consumed_food)
        user = request.user
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
        foods = Food.objects.all()
    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request, 'food/index.html', {'foods': foods, 'consumed_food': consumed_food})

