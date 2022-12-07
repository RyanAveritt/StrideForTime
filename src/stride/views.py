from django.http import HttpResponse
from django.shortcuts import render
from profiles.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home_view(request):
    statement = 'Welcome'
    user = request.user

    context = {
        'hello' : statement,    
        'user': user,
        'statement': "A stride for a better social environment by donating our time now!",
    }
    return render(request, 'main/home.html', context)
    # return HttpResponse('Hello world')