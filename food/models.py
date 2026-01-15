from django.db import models

# Create your models here.

"""
create table food (
    id integer primary key,
    name string
)
"""

class Category(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
       return f"{self.name}"

class Food(models.Model):
    photo = models.ImageField(blank=True, null=True, upload_to='food/')     
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
       return f"{self.name}"