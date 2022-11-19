from django.shortcuts import render, redirect
from .models import Calendar
from profiles.models import Profile

# Create your views here.
def my_calendar_view(request):
    calendar = Calendar.objects.filter(attendee=Profile.objects.get(user=request.user))
    context = {
        'calendar': calendar,
    }

    return render(request, 'calendars/mycalendar.html', context)
