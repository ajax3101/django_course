from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def about(request):
    print(request)
    return HttpResponse("Hello, world. You're about.")

def contact(request):
    print(request)
    return HttpResponse("You're CONTACT.")

def form(request):
    print(request)
    return HttpResponse("You're FORM.")
