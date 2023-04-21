from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home-view'),
    path('book/<str:title>/', views.book, name='book'),
    path('lesson_2/', include('lesson_2.urls')),
]