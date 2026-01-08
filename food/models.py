from django.db import models

# Create your models here.

"""
create table food (
    id integer primary key,
    name string
)
"""

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=500)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    

    def __str__(self):
       return f"{self.name}"