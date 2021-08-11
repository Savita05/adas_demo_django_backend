"""
This class is to write test cases for views.py file
"""
# from django.http import response
import pytest
from mixer.backend.django import mixer
from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from createuser.tests.test_setup import TestsetUp
# from createuser.models import loginprofile


@pytest.mark.django_db
class TestViews(TestsetUp):
    """Testing view Api's here"""

    def test_project_list_get(self):
        """Test project list api"""
        response = self.client.get(self.projectlist_url)
        self.assertEqual(response.status_code, 200)

    def test_registeredusers_get(self):
        """Test register api that fetches all user details """
        response = self.client.get(self.registerdusers_url)
        self.assertEqual(response.status_code, 200)

    def test_registerusers_post(self):
        """Test register users api"""
        res = self.client.post(self.registerdusers_url,
                               self.user_data, format="json")
        self.assertEqual(res.status_code, 200)

    def test_valid_login(self):
        """Test login api"""
        self.client.post(self.registerdusers_url,
                         self.user_data, format="json")
        res = self.client.post(self.login_url, self.user_data, format="json")
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code, 200)

    def test_delete_user(self):
        """Test the api can delete a users."""
        response = self.client.delete(
            reverse('register'),
            format='json',
            follow=True)
        # import pdb
        # pdb.set_trace()
        self.assertEqual(response.status_code, 204)

    def test_post_detail_is_authenticated(self):
        "Test if the user trying to access the view is authenticated"
        # mixer.blend('createuser.Post')
        url = reverse('regid', kwargs={'p_k': 3})
        request = RequestFactory().get(url)
        #request.user = self.user_data
        request.user = mixer.blend(User)
        response = self.client.get(request, p_k=3)
        self.assertEqual(response.status_code, 404)

    def test_delete_tasks(self):
        """Test the api can delete a tasks."""
        response = self.client.delete(
            reverse('tasks'),
            format='json',
            follow=True)
        # import pdb
        # pdb.set_trace()
        self.assertEqual(response.status_code, 204)
        
    def test_delete_projects(self):
        """Test the api can delete a project."""
        response = self.client.delete(
            reverse('project'),
            format='json',
            follow=True)
        # import pdb
        # pdb.set_trace()
        self.assertEqual(response.status_code, 204)
