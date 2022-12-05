from django import forms
from .models import Calendar
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class CalendarModelForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ('volunteer_type', 'start_time', 'end_time', 'location')
