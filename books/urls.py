"""test_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp

from django.contrib import admin
from django.urls import path
from django.views.decorators.http import condition

from books.views import (
    CreateBook, DeleteBook, GenreBooks, GenreBooksUpdate, ListBooks, ShowBook,
    UpdateBook, latest_entry,get_etag
)

app_name = 'books'

urlpatterns = [
    path('book/<int:pk>/', (condition(last_modified_func=latest_entry, etag_func=get_etag))
         (ShowBook.as_view()), name='book'),
    path('book/create/', CreateBook.as_view(), name='book_create'),
    path('book/update/<int:pk>/', UpdateBook.as_view(), name='book_update'),
    path('book/delete/<int:pk>/', DeleteBook.as_view(), name='book_delete'),
    path('', ListBooks.as_view(), name='book_all'),
    path('book/genres/update/<int:pk>/',
         GenreBooksUpdate.as_view(), name='books_genre_update'),
    path('book/genres/', GenreBooks.as_view(), name='books_genre'),

]
