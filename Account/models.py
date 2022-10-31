from django.db import models
from django.utils import timezone, dateformat

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    profileName = models.CharField(max_length=50, default="")
    bio = models.CharField(max_length=50, default="")
    email = models.EmailField()
    photo = models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=dateformat.format(timezone.now(), 'Y-m-d'))

    def __str__(self):
        return "%s %s" % (self.email, self.profileName)
    def fullName(self):
        return "%s %s" % (self.firstName, self.lastName)

