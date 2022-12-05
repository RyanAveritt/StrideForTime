from django.db import models
from profiles.models import Profile
from datetime import datetime


# Create your models here.
class Calendar(models.Model):
    class VolTypes(models.TextChoices):
        BUILD = "build"
        FOOD = "food"
        CLEAN = "clean"

    volunteer_type = models.CharField(max_length=5, choices=VolTypes.choices, blank=False)
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField( blank=False)
    #may want a sub model for location
    location = models.TextField(max_length=200, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    attendee = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='calendars')
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.attendee.user.username}_{self.volunteer_type}_{self.start_time.strftime('%m-%d-%Y')}-{self.end_time.strftime('%m-%d-%Y')}"

    def listCalendar(self):
        return f"{self.volunteer_type}_{self.location}_{duration(self,)}"
    def getEventTitle(self):
        return f'{self.volunteer_type}'
    def getEventStart(self):
        return f'{self.start_time}'
    def getEventEnd(self):
        return f'{self.end_time}'


def duration(self, interval = "default"):
    duration = self.end_time - self.start_time # For build-in functions
    duration_in_s = duration.total_seconds() 
    
    def years():
      return divmod(duration_in_s, 31536000) # Seconds in a year=31536000.

    def days(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 86400) # Seconds in a day = 86400

    def hours(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 3600) # Seconds in an hour = 3600

    def minutes(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 60) # Seconds in a minute = 60

    def seconds(seconds = None):
      if seconds != None:
        return divmod(seconds, 1)   
      return duration_in_s

    def totalDuration():
        y = years()
        d = days(y[1]) # Use remainder to calculate next variable
        h = hours(d[1])
        m = minutes(h[1])
        s = seconds(m[1])

        return "Duration: {} days, {} hours, {} minutes and {} seconds".format(int(d[0]), int(h[0]), int(m[0]), int(s[0]))

    return {
        'years': int(years()[0]),
        'days': int(days()[0]),
        'hours': int(hours()[0]),
        'minutes': int(minutes()[0]),
        'seconds': int(seconds()),
        'default': totalDuration()
    }[interval]