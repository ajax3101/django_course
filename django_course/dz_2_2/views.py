from django.shortcuts import render

def index(request):
    return render(request, 'dz_2_2/index.html')

def bio(request, username):
    user = {'username': username, 'bio': 'This is the bio of ' + username}
    return render(request, 'bio.html', {'user': user})
