from django import forms

from users.models import User

# from users.views import ShowLoginWindow


class ShowLoginWindowForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class EditLoginWindowForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'phone_number', 'birth_date']
