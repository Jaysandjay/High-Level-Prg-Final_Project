from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title

class User(models.Model):
    email= models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email