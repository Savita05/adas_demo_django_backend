"""this class is to test models.py"""

import pytest
#from mixer.backend.django import mixer
from createuser.models import assignTaskFiles, loginprofile

# pylint disable = C0115:


@pytest.mark.django_db
class TestModels:
    """testing login user """
    def test_post_create_user(self):
        """ method to test login user """
        loginprofile.objects.create(
        firstName="SK",
        password="Simple",
        role="maker",
        )

    def test_post_create_tasks(self):
        """ method to test taskfiles """
        assignTaskFiles.objects.create(
        File_Name = "123.mp4",
        project_name = "",
        Task_level = "",
        )

# @pytest.mark.django_db
# def test_model_display_title():
#     """ giving test"""
#     post = mixer.blend(loginprofile, firstName = "Testing")
#     assert (str(post) == "Testing")
