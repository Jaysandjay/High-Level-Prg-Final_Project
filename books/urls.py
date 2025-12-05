# books/urls.py
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:book_id>/', views.details, name="details"),
    path('add/', views.add, name="add"),
    path('edit/<int:book_id>/', views.edit, name="edit"),
    path('delete/<int:book_id>/', views.delete, name="delete"),
    path('search/', views.search_book, name="search_book"),
    path('', include('books.api.urls')),
]