from django.shortcuts import render, redirect
from .models import Calendar
from .forms import CalendarModelForm
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from statistics import mode, mean

from django.http import HttpResponse
from datetime import datetime
from django.template import loader
import json

# Create your views here.
@login_required
def my_calendar_view(request):
    calendar = Calendar.objects.filter(attendee=Profile.objects.get(user=request.user))
    event_list = []
    for event in calendar:
        title = event.location
        start = event.start_time
        end = event.end_time
        if end:
            event_dict = {'title':title, 'start':start, 'end':end}
        else:
            event_dict = {'title':title, 'start':start}
        event_list.append(event_dict)
    context = {
        'calendar': calendar,
        'fullcalendar': event_list
    }

    return render(request, 'calendars/mycalendar.html', context)

@login_required
def add_event_view(request):
    #deal with form here
    confirm = False
    form = CalendarModelForm()
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        form = CalendarModelForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.attendee = profile
            form.save()
            form = CalendarModelForm()
            confirm = True
        
    context = {
        'example_time': datetime.now().strftime("%Y-%m-%d %H:%M"),
        'form': form,
        'confirm': confirm
    }
    
    return render(request, 'calendars/event.html', context)

@login_required
def my_statistics_view(request):
    if request.method=='GET':
    #deal with stats here
        profile = Profile.objects.get(user=request.user)
        calendars = Calendar.objects.filter(attendee=profile)
        months = [c.start_time.month for c in calendars]
        month_mean = 'NA'
        month_mode = 'NA'
        if len(months) != 0:
            month_mean = mean(months).__round__()
            month_mode = mode(months)
        context = {
            'all_total': len(calendars),
            'build_total': len(calendars.filter(volunteer_type='build')),
            'food_total': len(calendars.filter(volunteer_type='food')),
            'clean_total': len(calendars.filter(volunteer_type='clean')),
            'friends_total': profile.get_friends_no(),
            'months_mean': month_mean,
            'months_mode': month_mode,
        }
        return render(request, 'calendars/statistics.html', context)
    return redirect('home-view')