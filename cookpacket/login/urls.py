""" Login page urls"""
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name = 'login'),
]