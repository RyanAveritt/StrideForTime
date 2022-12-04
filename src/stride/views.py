from django.http import HttpResponse
from django.shortcuts import render
from profiles.models import Profile
from django.contrib.auth.models import User

def home_view(request):
    statement = 'Welcome'
    user = request.user
    
    try:
        profile = Profile.objects.get(user=user)
        user = User.objects.get(username=user)
        print(profile.email)
        print(user.email)
    except:
        print(request.user)


    context = {
        'hello' : statement,    
        'user': user,
    }
    return render(request, 'main/home.html', context)
    # return HttpResponse('Hello world')