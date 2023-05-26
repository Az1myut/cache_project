from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView,
)
from icecream import ic

from books.utils import DataMixin

from .forms import EditLoginWindowForm
from .models import User

# Create your views here.


class ShowAllUsersWindow(DataMixin, ListView):
    # form_class = ShowLoginWindowForm
    model = User
    fields = '__all__'
    success_url = reverse_lazy('books:book_all')
    template_name = "users/users.html"
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['now'] = timezone.now()
        c_def = self.get_user_context(title="Пользователи")
        ic(c_def)
        return dict(list(context.items()) + list(c_def.items()))


class ShowLoginWindow(LoginRequiredMixin, TemplateView):
    # form_class = ShowLoginWindowForm
    model = User
    fields = '__all__'
    success_url = reverse_lazy('books:book_all')
    template_name = "users/login.html"

    # context_object_name = "login"

    # def get_object(self, request):
    #     """Метод возвращает пользователя"""

    #     return request.user

    # def get_context_data(self, **kwargs):
    #     """Метод получает и возвращает данные из формы"""
    #     context = super().get_context_data(**kwargs)
    #     context['user_form'] = ShowLoginWindowForm(
    #         instance=self.get_object(kwargs['request']))
    #     context['now'] = timezone.now()
    #     ic(context, context['user_form'])
    #     return context

    # def get(self, request, *args, **kwargs):
    #     """Метод возвращает шаблон с переданным словарём для выполнения"""
    #     self.object = self.get_object(request)
    #     return self.render_to_response(self.get_context_data(request=request))

    # def form_valid(self, form):
    #     """Метод проверки данных введённых в форме"""
    #     if form.is_valid():
    #         ic('valid', form)
    #         form.save(commit=False)
    #         form.save()
    #     else:
    #         return HttpResponseRedirect(self.get_success_url())
    #     # form.save()
    #     return HttpResponseRedirect(self.get_success_url())
    # # def form_valid(self, form):
    # #     return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     """
    #     Метод возвращает шаблон с переданным
    #     словарём или ошибку заполнения формы
    #     """
    #     self.object = self.get_object(request)
    #     form = self.get_form()
    #     self.form_valid(form)
    #     # user_form = ShowLoginWindow()
    #     #     return self.form_valid_formset(form, user_form)
    #     # else:
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class EditLoginWindow(DataMixin, LoginRequiredMixin, UpdateView):
    # form_class = ShowLoginWindowForm
    model = User
    fields = '__all__'
    success_url = reverse_lazy('books:book_all')
    template_name = "users/profile.html"
    # form_class = EditLoginWindowForm

    def get(self, request, *args, **kwargs):
        """Метод возвращает шаблон с переданным словарём для выполнения"""
        self.object = self.get_object(request)
        return self.render_to_response(self.get_context_data(request=request))

    def get_object(self, request):
        """Метод возвращает пользователя"""
        return request.user

    def post(self, request, *args, **kwargs):
        """
        Метод возвращает шаблон с переданным
        словарём или ошибку заполнения формы
        """
        self.object = self.get_object(request)
        form = self.get_form()
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = EditLoginWindowForm(
            instance=self.get_object(kwargs['request']))
        context['now'] = timezone.now()
        c_def = self.get_user_context(title="Редактировать профиль")
        ic(c_def)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return User.objects.all()
