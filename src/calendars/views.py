from django.shortcuts import render, redirect
from .models import Calendar
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template import loader
import json

# Create your views here.
@login_required
def my_calendar_view(request):
    calendar = Calendar.objects.filter(attendee=Profile.objects.get(user=request.user))
    event_list = []
    for event in calendar:
        title = event.volunteer_type
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
    #deal with form here, ref profile my_profile_view
    context = {
        'event': "sample",
    }
    return render(request, 'calendars/event.html', context)

@login_required
def my_statistics_view(request):
    #deal with stats here
    context = {
        'mean': "sample",
        'length': "sample",
    }
    return render(request, 'calendars/statistics.html', context)
