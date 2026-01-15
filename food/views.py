from django.shortcuts import render
from .models import Food

# Create your views here.

"""
select * from food;
"""

# food = """
#     select * from product where name = '{user_input}';
# """

"""
select * from food ILIKE where "%free%"
"""

def home(request):
    return render(request, 'base.html')


def food_list(request):
    foods = Food.objects.all()
    return render(request, 'foods/food_list.html', context={'foods': foods})
    

def food_detail(request, food_id):
    food = Food.objects.filter(id=food_id).first()
    return render(request, 'foods/food_detail.html', context={'food': food})

