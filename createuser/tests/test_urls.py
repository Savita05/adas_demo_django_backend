"""
this class is to test for urls of createuser app
"""

from django.test import SimpleTestCase
from django.urls import resolve, reverse
from createuser.views import (projectfiles_id, register_users, Login, registerdusers_id, scenelevelattributes_id, taskfiles_list, scenelevelattributes,
                              objectlevelattributes, project_files, taskfileslist_id,
                              objectlevelattributes_id)


class TestUrls(SimpleTestCase):
    """
    Here testing different urls
    """

    def test_login_url(self):
        """
        returns 200 if login post url is valid
        """
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, Login)

    def test_add_url(self):
        """
        returns 200 if register post/get/delete url is valid
        """
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_users)

    def test_tasks_url(self):
        """
        returns 200 if task post/delete/get url is valid
        """
        url = reverse('tasks')
        self.assertEqual(resolve(url).func, taskfiles_list)

    def test_scenlevel_url(self):
        """
        returns 200 if scenelevel post/get/delete url is valid
        """
        url = reverse('sceneLevel')
        self.assertEqual(resolve(url).func, scenelevelattributes)

    def test_objectlevel_url(self):
        """
        returns 200 if objectlevel post/get/delete url is valid
        """
        url = reverse('objectLevel')
        self.assertEqual(resolve(url).func, objectlevelattributes)

    def test_projectfiles_url(self):
        """
        returns 200 if project post/get/delete url is valid
        """
        url = reverse('project')
        self.assertEqual(resolve(url).func, project_files)

    def test_post_taskid_url(self):
        """Test api based on task id
        test case passes only if pattern is <p_k>[0-9]
        """
        url = reverse('taskid', kwargs={'p_k': 1})
        self.assertEqual(resolve(url).func, taskfileslist_id)

    def test_post_registerid_url(self):
        """Test api based on task id
        test case passes only if pattern is <p_k>[0-9]
        """
        url = reverse('regid', kwargs={'p_k': 1})
        self.assertEqual(resolve(url).func, registerdusers_id)

    def test_post_objlevelid_url(self):
        """Test api based on object id
        test case passes only if pattern is <p_k>[0-9]
        """
        url = reverse('objectlid', kwargs={'p_k': 1})
        self.assertEqual(resolve(url).func, objectlevelattributes_id)

    def test_projectfileid_url(self):
        """Test api based on project id
        test case passes only if pattern is <p_k>[0-9]
        """
        url = reverse('projectid', kwargs={'p_k': 1})
        self.assertEqual(resolve(url).func, projectfiles_id)

    def test_scenlvlid_url(self):
        """Test api based on scenelevel id
        test case passes only if pattern is <p_k>[0-9]
        """
        url = reverse('scenelevelid', kwargs={'p_k': 1})
        self.assertEqual(resolve(url).func, scenelevelattributes_id)
