from django.urls import path, re_path
from lesson_11 import views



urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    
    ]