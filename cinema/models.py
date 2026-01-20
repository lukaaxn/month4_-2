from django.db import models

# Create your models here.

"""
create table movie (
    id integer primary key,
    title string
)
"""

class Genre(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
       return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    poster = models.ImageField(blank=True, null=True, upload_to='cinema/')     
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    ticket_price = models.IntegerField(default=500)
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, null=True, blank=True
    )
    tag = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
       return f"{self.title}"

