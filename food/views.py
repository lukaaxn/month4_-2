
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.decorators.http import require_GET
from .form import FoodForm, SearchForm
from .models import Food

# Простая реализация добавления в корзину через сессию
@login_required(login_url='/login/')
@require_GET
def add_to_cart_view(request, food_id):
    cart = request.session.get('cart', [])
    if food_id not in cart:
        cart.append(food_id)
        request.session['cart'] = cart
    return HttpResponse('Добавлено в корзину!')

@login_required(login_url='/login/')
def food_delete_view(request, food_id):
    food = Food.objects.filter(id=food_id).first()
    if not food:
        return HttpResponse('Блюдо не найдено', status=404)
    if request.method == 'POST':
        food.delete()
        return HttpResponse('Блюдо удалено')
    return render(request, 'foods/food_confirm_delete.html', {'food': food})

# Create your views here.

"""
select * from movie;
"""
# movie = """
#     select * from movie where title = '{user_input}';
# """
"""
select * from movie ILIKE where "%drama%"
"""

"""
insert into movie (title, description, ticket_price) values ('title', 'description', 500);
"""

# GET - для просмотра данных
# POST - для отправки данных
# PUSH - для обновления данных
# PATCH - для частичного обновления данных
# DELETE - для удаления данных


# lt - movie's ticket_price < 500
# gt - movie's ticket_price > 500
# lte - movie's ticket_price <= 500
# gte - movie's ticket_price >= 500


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
            Q(title__icontains=search) | Q(description__icontains=search)
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
    max_page = range(1, foods.count() // limit + 2)
    if page:
        foods = foods[limit * (int(page) - 1) : limit * int(page)]
    return render(
        request,
        'foods/food_list.html', 
        context={'foods': foods, 'form': forms, 'max_page': max_page},
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
            Food.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                photo=form.cleaned_data['photo'],                
            )
            return HttpResponse('Food created')
        return HttpResponse('Invalid form')



