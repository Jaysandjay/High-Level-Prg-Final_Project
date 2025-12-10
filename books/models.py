from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(9999)],
        help_text="Enter a 4-digit year (e.g., 2024)"
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Enter a rating between 1 and 10"
    )
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
