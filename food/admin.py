from django.contrib import admin

from food.models import Food, Category, Tag

# Register your models here.
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Tag)