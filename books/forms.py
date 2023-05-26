from dataclasses import fields
import imp
from django import forms
from books.models import Book
from books.views import CreateBook


class CreateBook(forms.ModelForm):
    class Meta:
        fields = '__all__'
