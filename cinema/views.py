
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .form import MovieForm, SearchForm
from .models import Movie

@login_required(login_url='/login/')
def movie_delete_view(request, movie_id):
    movie = Movie.objects.filter(id=movie_id).first()
    if not movie:
        return HttpResponse('Фильм не найден', status=404)
    if request.method == 'POST':
        movie.delete()
        return HttpResponse('Фильм удалён')
    return render(request, 'cinema/movie_confirm_delete.html', {'movie': movie})

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
def movie_list(request):
    limit = 3
    movies = Movie.objects.all()
    forms = SearchForm()
    search = request.GET.get('search') or request.POST.get('search', '')  
    genre = request.GET.get('genre') or request.POST.get('genre', '')
    price = request.GET.get('price') or request.POST.get('price', '')
    tags = request.GET.getlist('tags') or request.POST.getlist('tags', [])
    ordering = request.GET.get('ordering') or request.POST.get('ordering', '')
    page = request.GET.get('page')
    if genre:
        movies = movies.filter(genre=genre)
    if search:
        movies = movies.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )
    if price:
        if price == '1':
            movies = movies.filter(ticket_price__lt=500)
        elif price == '2':
            movies = movies.filter(ticket_price__gt=500)

    if tags:
        movies = movies.filter(tag__in=tags).distinct()

    if ordering:
        movies = movies.order_by(ordering)
    max_page = range(movies.count() // limit + 1)
    if page:
        movies = movies[limit * (int(page) - 1) : limit * int(page)]
    return render(
        request,
        'cinema/movie_list.html', 
        context={'movies': movies, 'form': forms, 'max_page': max_page[1:]},
    )


@login_required(login_url='/login/')
def movie_detail(request, movie_id):
    if request.method == 'GET':
        movie = Movie.objects.filter(id=movie_id).first()
        return render(
            request, 'cinema/movie_detail.html', context={'movie': movie}
        )

@login_required(login_url='/login/')
def movie_create_view(request):
    if request.method == 'GET':
        form = MovieForm()
        return render(request, 'cinema/movie_create.html', context={'form': form})
    elif request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.clean_data)
            Movie.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                ticket_price=form.cleaned_data['ticket_price'],
                poster=form.cleaned_data['poster'],                
            )
        return HttpResponse('Movie created')



