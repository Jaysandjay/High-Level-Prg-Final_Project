from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('details/<int:book_id>/', views.details, name="details"),
    path('add/', views.add, name="add"),
    path('edit/<int:book_id>/', views.edit, name="edit"),
    path('delete/<int:book_id>/', views.delete, name="delete"),
]