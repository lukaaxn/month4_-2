from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .form import FoodForm, SearchForm
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


# lt - food's price < 500
# gt - food's price > 500
# lte - food's price <= 500
# gte - food's price >= 500


def home(request):
    if request.method == 'GET':
        return render(request, 'base.html')


@login_required(login_url='/login/')
def food_list(request):
    limit = 3
    foods = Food.objects.all()
    forms = SearchForm()
    search = request.GET.get('search') or request.POST.get('search', '')  
    category = request.GET.get('category') or request.POST.get('category', '')
    price = request.GET.get('price') or request.POST.get('price', '')
    tags = request.GET.getlist('tags') or request.POST.getlist('tags', [])
    ordering = request.GET.get('ordering') or request.POST.get('ordering', '')
    page = request.GET.get('page')
    if category:
        foods = foods.filter(category=category)
    if search:
        foods = foods.filter(
            Q(name__icontains=search) | Q(description__icontains=search)
        )
    if price:
        if price == '1':
            foods = foods.filter(price__lt=500)
        elif price == '2':
            foods = foods.filter(price__gt=500)

    if tags:
        foods = foods.filter(tag__in=tags).distinct()

    if ordering:
        foods = foods.order_by(ordering)
    max_page = range(foods.count() // limit + 1)
    if page:
        foods = foods[limit * (int(page) - 1) : limit * int(page)]
    return render(
        request,
        'foods/food_list.html', 
        context={'foods': foods, 'form': forms, 'max_page': max_page[1:]},
    )


@login_required(login_url='/login/')
def food_detail(request, food_id):
    if request.method == 'GET':
        food = Food.objects.filter(id=food_id).first()
        return render(
            request, 'foods/food_detail.html', context={'food': food}
        )

@login_required(login_url='/login/')
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



