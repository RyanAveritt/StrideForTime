from django.urls import path
from .views import my_calendar_view

app_name = 'calendars'

urlpatterns = [
    path('', my_calendar_view, name='my-calendar-view'),
]