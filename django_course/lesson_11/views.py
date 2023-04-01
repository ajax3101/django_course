from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'lesson_1_1/index.html')

def hello(request):
    print(request)
    return HttpResponse("Hello, World!")