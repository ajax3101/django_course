from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("направляє URL з home/' у метод views.home і задає ім'я для цього URL як 'home-view';")

def book(request, title):
    return HttpResponse(f"You are reading {title}.")
