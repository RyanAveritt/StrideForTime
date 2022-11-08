from django.test import TestCase
from .models import Calendar
from django.contrib.auth.models import AnonymousUser, User
import datetime

# Create your tests here.
class AccountTestCase(TestCase):        
    # def setup(self):
    #     number_of_entries= 13
    #     for entry in range(number_of_entries):
    #         Calendar.objects.create(
    #             user=User(email=f'test{entry}@me.com', password='password'),
    #             start_time=f'2022-{number_of_entries-entry}-02 11:11:51.000000',
    #             end_time=f'2022-{number_of_entries+entry}-02 11:11:51.000000',
    #             location=f'Alachua Habitat for Humanity',
    #             volunteer_type=f'build',
    #         )
    def test_instance_time(self):
        entry1 = Calendar(
            start_time=datetime.datetime(2022, 10, 2, 11, 11, 51),
            end_time=datetime.datetime(2022, 10, 2, 13, 11, 51),
            location=f'Alachua Habitat for Humanity',
            volunteer_type=f'build',
        )
        self.assertEqual(str(entry1.duration()), "2:00:00")

        entry2 = Calendar(
            start_time=datetime.datetime(2022, 10, 2, 11, 11, 51),
            end_time=datetime.datetime(2022, 10, 4, 11, 11, 51),
            location=f'Alachua Habitat for Humanity',
            volunteer_type=f'build',
        )
        self.assertEqual(str(entry2.duration()), "2 days, 0:00:00")

    def test_type(self):
        entry = Calendar(
            start_time=datetime.datetime(2022, 10, 2, 11, 11, 51),
            end_time=datetime.datetime(2022, 10, 2, 13, 11, 51),
            location=f'Alachua Habitat for Humanity',
            volunteer_type=f'build',
        )
        self.assertEqual(entry.volunteer_type, "build")

    def test_location(self):
        entry = Calendar(
            start_time=datetime.datetime(2022, 10, 2, 11, 11, 51),
            end_time=datetime.datetime(2022, 10, 2, 13, 11, 51),
            location=f'Alachua Habitat for Humanity',
            volunteer_type=f'build',
        )
        self.assertEqual(entry.location, "Alachua Habitat for Humanity")

