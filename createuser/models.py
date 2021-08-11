"""
For createuser app created a login database and different
collections are listed here
C0103: Variable name "" doesn't conform to snake_case naming style (invalid-name)
"""
# pylint: disable=C0103
from django.db import models

def upload_path(File_Name):
    """
    this method to save uploaded files with
    param fine name
    """
    return '/'.join([File_Name])

# Create your models here.


class assignTaskFiles(models.Model):
    """
    assigntaskfiles collection is having below records
    """
    File_Name = models.CharField(max_length=100, blank=False)
    project_name = models.TextField(null=True, blank=True)
    Task_level = models.TextField(null=True, blank=True)
    Priority = models.TextField(null=True, blank=True)
    Created_Date = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    Action = models.TextField(null=True, blank=True)
    annotation_image = models.ImageField(
        blank=True, null=True, upload_to=upload_path)


class loginprofile(models.Model):
    """
    loginprofile collection is having below records
    """
    firstName = models.TextField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)
    role = models.TextField(blank=True)

def __str__(self):
    return self.firstName

class objectLevel(models.Model):
    """
    objectLevel collection is having below records
    """
    trackId = models.TextField(null=True, blank=True)
    objectClass = models.TextField(null=True, blank=True)
    occlusion = models.TextField(null=True, blank=True)
    pose = models.TextField(null=True, blank=True)
    lane_change = models.BooleanField(null=True, blank=True)
    breakLight = models.BooleanField(null=True, blank=True)


class SceneLevel(models.Model):
    """
    SceneLevel collection is having below records
    """
    Light_Condition = models.TextField(null=True, blank=True)
    Road_Type = models.TextField(null=True, blank=True)
    Road_works = models.TextField(null=True, blank=True)
    Tunnel = models.TextField(null=True, blank=True)
    Weather = models.TextField(null=True, blank=True)
    Street_Condition = models.TextField(null=True, blank=True)


class ProjectFiles(models.Model):
    """
    ProjectFiles collection is having below records
    """
    project_name = models.TextField(null=True, blank=True)
    project_Feature = models.TextField(null=True, blank=True)
    Tool_version = models.TextField(null=True, blank=True)


class Objectcategories(models.Model):
    """
    Objectcategories collection is having below records
    """
    object_category = models.TextField(null=True, blank=True)


# class userprofile(models.Model):
#     """
#     loginprofile collection is having below records
#     """
#     firstName = models.TextField(null=True, blank=True)
#    # lastname = models.TextField(null=True, blank=True)
#     password = models.TextField(null=True, blank=True)
#     role = models.TextField(blank=True)
