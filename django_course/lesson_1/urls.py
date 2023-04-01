from django.urls import path, re_path
from lesson_1 import views



urlpatterns = [
    path('', views.index, name='home'),
    ]