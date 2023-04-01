from django.urls import path, re_path
from lesson_2 import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    re_path(r'^about/', views.about),
    re_path(r'^contact/', views.contact),
    re_path(r'^form/', views.form),

]
