from django.urls import path
from .views import my_calendar_view, my_statistics_view, add_event_view

app_name = 'calendars'

urlpatterns = [
    path('', my_calendar_view, name='main-calendar-view'),
    path('event/', add_event_view, name='add-event-view'),
    path('statistics/', my_statistics_view, name='statistics-view'),
]