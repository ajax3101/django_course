from django.urls import path, re_path
from weather import views


urlpatterns = [

    path('', views.index, name='home_weather'),
    #path('/weather/?city=', views.weather, name='weather'),
    re_path(r'^weather/', views.weather),
]
