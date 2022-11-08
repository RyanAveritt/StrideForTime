from django.db import models
from profiles.models import Profile

# Create your models here.
class Calendar(models.Model):
    class VolTypes(models.TextChoices):
        BUILD = "build"
        FOOD = "food"
        CLEAN = "clean"
        
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='calendars')
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField( blank=False)
    location = models.TextField(max_length=200, blank=False)
    volunteer_type = models.CharField(max_length=5, choices=VolTypes.choices, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.volunteer_type}_{self.location}_{self.start_time.strftime('%m-%d-%Y')}-{self.end_time.strftime('%m-%d-%Y')}"

    def duration(self):
        duration = self.end_time-self.start_time
        return duration
