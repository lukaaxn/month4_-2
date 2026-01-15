from django import forms
blackl_list = [
    'BadFood',
    'UglyFood', 
    'NastyFood'
]

class FoodForm(forms.Form):
    name = forms.CharField(max_length=50, min_length=3)
    description = forms.CharField(max_length=150)
    price = forms.IntegerField()
    photo = forms.ImageField()

   