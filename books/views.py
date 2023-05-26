from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control, cache_page
from django.views.decorators.http import condition, etag, last_modified
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView,
)
from icecream import ic

from .models import Book, Genre
from .utils import DataMixin

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
# @method_decorator(cache_control(max_age=0), name='dispatch')


class GenreBooks(DataMixin, ListView):
    model = Genre
    template_name = "pages/genres/genres_all.html"
    paginate_by = 10
    fields = '__all__'
    context_object_name = "genres"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        ic(context)
        c_def = self.get_user_context(title="Жанры")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Genre.objects.all()


class GenreBooksUpdate(SuccessMessageMixin, UpdateView):
    model = Genre
    template_name = 'pages/genres/genre_update.html'
    fields = '__all__'
    template_name_suffix = '_update_genre_form'
    success_url = reverse_lazy('books:books_genre')
    success_message = "Жанр: \"%(genre)s\" сохранён"


def latest_entry(request, pk):
    ic(pk)
    pub_date = Book.objects.filter(pk=pk).first()
    ic(pub_date)
    return pub_date.pub_date


def get_last_modified(request, *args, **kwargs):
    return timezone.now()


def get_etag(request, *args, **kwargs):
    # etag = request.get_full_path()+str(timezone.now())
    etag = 'asdadm1'
    return etag


class ShowBook(DataMixin, DetailView):
    model = Book
    template_name = "pages/book.html"
    paginate_by = 10
    context_object_name = "book"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Книга")
        return dict(list(context.items()) + list(c_def.items()))

# @method_decorator(cache_control(max_age=0), name='dispatch')


class CreateBook(DataMixin, SuccessMessageMixin, CreateView):
    model = Book
    template_name = "pages/book_create.html"
    template_name_suffix = '_create_form'
    fields = '__all__'
    success_url = reverse_lazy('books:book_all')
    success_message = "Книга: %(name)s создана"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Новая книга")
        return dict(list(context.items()) + list(c_def.items()))

# @method_decorator(cache_page(CACHE_TTL), name='dispatch')
# @method_decorator(last_modified(get_last_modified), name='dispatch')
# @method_decorator(etag(get_etag), name='dispatch')


class ListBooks(DataMixin, ListView):
    model = Book
    template_name = "pages/book_all.html"
    paginate_by = 10
    fields = '__all__'
    context_object_name = "books"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Book.objects.filter(is_published=True)


# @method_decorator(condition(last_modified_func=latest_entry), name='dispatch')


class UpdateBook(DataMixin, SuccessMessageMixin, UpdateView):
    model = Book
    template_name = 'pages/book_update.html'
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('books:book_all')
    success_message = "Книга: %(name)s сохранена"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обновить страницу")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Book.objects.filter(is_published=True)


class DeleteBook(SuccessMessageMixin, DeleteView):
    template_name = 'pages/book_delete.html'
    success_message = "Книга: %(name)s удалена"
    success_url = reverse_lazy('books:book_all')

    def get_object(self) -> Book:
        pk_ = self.kwargs.get('pk')

        return get_object_or_404(Book, pk=pk_)

    # def get_success_url(self) -> str:
    #     return reverse('books:book_all')

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )
