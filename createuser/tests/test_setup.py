
"""
this setup file is for storing common urls and
for testing dummy data
"""
from rest_framework.test import APITestCase
from django.urls import reverse
# from Faker import faker


class TestsetUp(APITestCase):
    """
    testing set up file for both urls and
    dummy data
    """
    def setUp(self):
        self.registerdusers_url = reverse('register')
        self.login_url = reverse('login')
        self.projectlist_url = reverse('project')
        # self.fake = Faker()

        self.user_data={
            'firstName':"name",
            'password': "savita",
            'role':"maker"
        }
        return super().setUp()

def teardown(self):
    """method to destry table"""
    return self.super().tearDown()
