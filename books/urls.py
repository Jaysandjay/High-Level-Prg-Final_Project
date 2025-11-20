from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:book_id>/', views.details, name="details"),
    path('add/', views.add, name="add"),
    path('edit/<int:book_id>/', views.edit, name="edit"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('delete/<int:book_id>/', views.delete, name="delete"),
]