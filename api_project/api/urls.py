from django.urls import path, include
from .views import BookList, BookViewSet
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
