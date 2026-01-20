from django import forms

from .models import Genre, Tag


class MovieForm(forms.Form):
    title = forms.CharField(max_length=50, min_length=3)
    description = forms.CharField(max_length=150)
    ticket_price = forms.IntegerField()
    poster = forms.ImageField()


class SearchForm(forms.Form):
    ordering = [
        ('created_at', 'Created_At'), 
        ('updated_at', 'Updated_At'), 
        ('ticket_price', 'Price'), 
        ('title', 'Title'),
        ('-created_at', 'Created_At(descinding)'), 
        ('-updated_at', 'Updated_At(descinding)'), 
    ]
    search = forms.CharField(max_length=100, required=False)
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    ordering = forms.ChoiceField(choices=ordering, required=False)

    # random = forms.MultipleChoiceField(choices=random_list, required=False)