from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from Account.models import User

# Create your tests here.
class AccountTestCase(TestCase):        
    def setup(self):
        # email, password, firstname, lastname, bio, joinDate, photo
        User.objects.create(email="test@me.com", password="123987", firstName="John", lastName="Doe", bio="I like sleeping", photo="johnDoe.jpg")
        User.objects.create(email="Rav@me.com", password="test", firstName="Ryan", lastName="Averitt", bio="CS Student", photo="ryan.jpg")

    def test_instance(self):
        self.setup()
        user1 = User.objects.get(email="test@me.com")
        self.assertTrue(isinstance(user1, User))

    def test_getting_acct_info(self):
        self.setup()
        user1 = User.objects.get(email="test@me.com")
        self.assertEqual(user1.fullName(), 'John Doe')
        user2 = User.objects.get(email="Rav@me.com")
        self.assertEqual(user2.fullName(), 'Ryan Averitt')
    
    def test_getting_acct_info_fail(self):
        self.setup()
        user1 = User.objects.get(email="test@me.com")
        self.assertEqual(user1.fullName(), 'Ryan Averitt')

