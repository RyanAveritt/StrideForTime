from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client
from django.urls import reverse

from .models import Profile

# Create your tests here.
class AccountTestCase(TestCase):        
    # def setup(self):
        # email, first_name, last_name, bio
        # number_of_profiles = 13
        # Profile.objects.create(id=1, email='test@me.com', first_name="John", last_name="Doe", location= "Florida", bio='no bio set')

        # for pid in range(number_of_profiles):
        #     Profile.objects.create(
        #         email=f'test{pid}@me.com',
        #         first_name=f'John{pid}',
        #         last_name=f'Doe{pid}',
        #     )
    # def test_instance(self):
        # print(Profile.objects.first())
        # self.assertTrue(isinstance(prf1, Profile))

    def test_getting_acct_info(self):
        prf1 = Profile(email='test@me.com', first_name="John", last_name="Doe")
        self.assertEqual(prf1.fullName(), 'John Doe')
        prf2 = Profile(email='tester@me.com', first_name="Doe", last_name="John")
        self.assertEqual(prf2.fullName(), 'Doe John')
    
    def testing_account_register_login_logout(self):
        c = Client()
        response = c.post('/register', {'username': 'Az', 'email': 'test@me.com', 'password': 'n6q022To&0Y9&0Y9th'})
        self.assertEqual(response.status_code, 200)
        response = c.post('/login', {'username': 'Az', 'password': 'n6q022To&0Y9&0Y9th'})
        self.assertEqual(response.status_code, 200)
        response = c.get('/logout')
        self.assertEqual(response.status_code, 302)
    
    def testing_account_register_login_false_password(self):
        c = Client()
        response = c.post('/register', {'username': 'Az', 'email': 'test@me.com', 'password': 'n6q022To&0Y9&0Y9th'})
        self.assertEqual(response.status_code, 200)
        response = c.post('/login', {'username': 'Az', 'password': 'false_password'})
        self.assertEqual(response.status_code, 200)

    def testing_account_register_login_false_username(self):
        c = Client()
        response = c.post('/register', {'username': 'Az', 'email': 'test@me.com', 'password': 'n6q022To&0Y9&0Y9th'})
        self.assertEqual(response.status_code, 200)
        response = c.post('/login', {'username': 'false_username', 'password': 'password'})
        self.assertEqual(response.status_code, 200)



