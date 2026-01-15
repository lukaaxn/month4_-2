from django.http import HttpResponse
from django.shortcuts import render

from .form import FoodForm

from .models import Food

# Create your views here.

"""
select * from food;
"""

# food = """
#     select * from food where name = '{user_input}';
# """

"""
select * from food ILIKE where "%free%"
"""

"""
insert into food (name, description, price) values ('name', 'description', 500);
"""


# GET - для просмотра данных
# POST - для отправки данных
# PUSH - для обновления данных
# PATCH - для частичного обновления данных
# DELETE - для удаления данных


def home(request):
    if request.method == 'GET':
        return render(request, 'base.html')


def food_list(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        return render(request, 'foods/food_list.html', context={'foods': foods})
    

def food_detail(request, food_id):
    if request.method == 'GET':
        food = Food.objects.filter(id=food_id).first()
        return render(
            request, 'foods/food_detail.html', context={'food': food}
        )
    
def food_create_view(request):
    if request.method == 'GET':
        form = FoodForm()
        return render(request, 'foods/food_create.html', context={'form': form})
    elif request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.clean_data)
            Food.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                photo=form.cleaned_data['photo'],                
            )
        return HttpResponse('Food created')



