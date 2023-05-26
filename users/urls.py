from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from .views import EditLoginWindow, ShowAllUsersWindow, ShowLoginWindow

app_name = 'user'

urlpatterns = [
    path('login/', ShowLoginWindow.as_view(), name='login'),
    path('edit/<int:pk>', EditLoginWindow.as_view(), name='edit'),
    path('users/', ShowAllUsersWindow.as_view(), name='users'),
]
