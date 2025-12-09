# books/api/urls.py
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', views.BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('books/<int:id>/', views.BookDetailAPIView.as_view(),
         name='book-detail-api'),
]
