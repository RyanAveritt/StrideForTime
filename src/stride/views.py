from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    statement = 'Welcome (still in dev)'
    user = request.user

    context = {
        'hello' : statement,    
        'user': user,
    }
    return render(request, 'main/home.html', context)
    # return HttpResponse('Hello world')