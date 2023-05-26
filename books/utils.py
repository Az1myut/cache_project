from icecream import ic

from .models import Genre

menu = [{'title': "Главная", 'url_name': 'books:book_all'},
        {'title': "Добавить книгу", 'url_name': 'books:book_create'},
        {'title': "Посмотреь жанры", 'url_name': 'books:books_genre'},
        {'title': "Users", 'url_name': 'user:users'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        user_menu = menu.copy()

        if not self.request.user.is_authenticated:
            user_menu.pop(3)
        context = kwargs
        genre = Genre.objects.all()
        context['menu'] = user_menu
        context['genre'] = genre

        return context
