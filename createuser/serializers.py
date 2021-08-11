"""
This file is to write serializers for createuser
"""
from rest_framework import serializers
from createuser.models import (ProjectFiles, SceneLevel, assignTaskFiles,
                               loginprofile, objectLevel,  Objectcategories)

# pylint disable=R0903
# pylint disable=C0115

class LoginSerializer(serializers.ModelSerializer):
    """
    Login serializer with firstname , password and role details
    """
    class Meta:
        model = loginprofile
        fields = '__all__'


class ObjectcategoriesSerializer(serializers.ModelSerializer):
    """
    object category serializer
    """
    class Meta:
        model = Objectcategories
        fields = ('id',
              'object_category')


class ObjectLevelSerializer(serializers.ModelSerializer):
    """
    object level list serializer
    """
    class Meta:
        model = objectLevel
        fields = ('id',
              'trackId', 'objectClass', 'occlusion',
              'pose', 'lane_change', 'breakLight')


class SceneLevelSerializer(serializers.ModelSerializer):
    """
    scene level serializer
    """
    class Meta:
        model = SceneLevel
        fields = ('id',
              'Light_Condition', 'Road_Type', 'Road_works',
              'Tunnel', 'Weather', 'Street_Condition')


class ProjectFilesSerializer(serializers.ModelSerializer):
    """
    project files serializer
    """
    class Meta:
        model = ProjectFiles
        fields = ('id',
              'project_name', 'project_Feature', 'Tool_version')


class TaskFilesSerializer(serializers.ModelSerializer):
    """
    Task files serializer
    """
    class Meta:
        model = assignTaskFiles
        fields = ('id',
              'File_Name', 'project_name', 'Task_level', 'Priority',
              'Created_Date', 'status', 'Action', 'annotation_image')
