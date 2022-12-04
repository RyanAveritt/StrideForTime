from django.shortcuts import render, redirect
from .models import Calendar
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def my_calendar_view(request):
    calendar = Calendar.objects.filter(attendee=Profile.objects.get(user=request.user))
    context = {
        'calendar': calendar,
    }

    return render(request, 'calendars/mycalendar.html', context)
