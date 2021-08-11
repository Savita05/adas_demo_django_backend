
"""
This file is to write API for logic part like register user, login user and other methods
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
#from django.core.files import File
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
from createuser.serializers import (LoginSerializer, TaskFilesSerializer,
                                    ObjectcategoriesSerializer, ObjectLevelSerializer,
                                    SceneLevelSerializer, ProjectFilesSerializer)
from createuser.models import (assignTaskFiles, loginprofile, objectLevel,
                               SceneLevel, ProjectFiles,
                               Objectcategories)


# from django.contrib.auth import authenticate, login
# from django.shortcuts import render


@api_view(['GET', 'POST', 'DELETE'])
def register_users(request):
    """
    This method allows new users to register for logging to ADAS tool
    """
    if request.method == 'POST':
        obj = loginprofile()
        obj.firstName = request.data['firstName']
        obj.role = request.data['role']
        obj.password = request.data['password']
        obj.save()
        return Response("Saved successfully", None)

    if request.method == 'GET':
        registered_names = loginprofile.objects.all().values()
        return Response(registered_names)

    else:
        #request.method == 'DELETE'
        count = loginprofile.objects.all().delete()
        return JsonResponse({'message': '{} users deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def registerdusers_id(request, p_k):
    """
    This method is based on id to fetch, delete , and update users
    """
    try:
        registerednames = loginprofile.objects.get(pk=p_k)
    except loginprofile.DoesNotExist:
        return JsonResponse(
            {'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        users_serializer = LoginSerializer(registerednames)
        return JsonResponse(users_serializer.data)

    if request.method == 'PUT':
        cat_data = JSONParser().parse(request)
        print(cat_data)
        users_serializer = LoginSerializer(registerednames, data=cat_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data)
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        registerednames.delete()
        return JsonResponse(
            {'message': 'user was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class Login(APIView):
    """
    Class is for logging users
    """

    def post(self, request):
        """
        Based on registered users, this method allows to login in to the tool
        if correct credentials then user is logged successfully
        else gives error message as 'invalid credentials'
        """
        # if request.method == 'POST':
        cred = request.data
        name = request.data['firstName']
        password = request.data['password']
        # role=request.data['role']
        print("cred", cred)
        check = loginprofile.objects.filter(
            firstName=name, password=password).values()
        if check:
            result = {
                'status': '200',
                'message': 'Login Successfull'
            }
            return JsonResponse(result)

        # elif (check != ("/^[0-9]") ):
        #     print("enetering elif loop")
        #     result = {'status': '401',
        #         'message': 'invalid inputs'
        #     }
        #     return JsonResponse(result)

        elif not check:
            return Response('Invalid credentials', status=status.HTTP_401_UNAUTHORIZED)


class Getuser(APIView):
    """
    class is for fetching users
    """

    def getusers(self, request):
        """
        This method fetches all the users registered
        """
        if request.method == 'GET':
            print(request.data)
            entry = loginprofile.objects.all().values()
            print("entry", entry)
            return Response(entry)


@api_view(['GET'])
def getproject_name(request):
    """
    This method is to return only the list of
    project names from projectFiles collection
    """
    if request.method == 'GET':
        entry = ProjectFiles.objects.values("project_name")
        return Response(entry)

# writing get, put, delete, post methods for objectlevelAtrributes


@api_view(['GET', 'POST', 'DELETE'])
def objectlevelattributes(request):
    """
    This method is to add object level attributes
    """
    if request.method == 'POST':
        obj = objectLevel()
        obj.trackId = request.data['trackId']
        obj.objectClass = request.data['objectClass']
        obj.pose = request.data['pose']
        obj.occlusion = request.data['occlusion']
        obj.lane_change = request.data['lane_change']
        obj.breakLight = request.data['breakLight']
        obj.save()
        return Response("Saved successfully")

    if request.method == 'GET':
        getobjectlevelattributes = objectLevel.objects.all().values()
        return Response(getobjectlevelattributes)

    else:
        #request.method == 'DELETE'
        count = objectLevel.objects.all().delete()
        return JsonResponse(
            {'message': '{} objectLevelAttributes  deleted successfully!'.format(
                count[0])},
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def objectlevelattributes_id(request, p_k):
    """
    Different operations are performed on object level attributes based on id
    """
    try:
        objectlevelatrributeslist = objectLevel.objects.get(pk=p_k)
    except objectLevel.DoesNotExist:
        return JsonResponse(
            {'message': 'The objectLevelAttributes does not exist'},
            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        objlevelserializer = ObjectLevelSerializer(objectlevelatrributeslist)
        return JsonResponse(objlevelserializer.data)

    if request.method == 'PUT':
        cat_data = JSONParser().parse(request)
        print(cat_data)
        objlevelserializer = ObjectLevelSerializer(
            objectlevelatrributeslist, data=cat_data)
        if objlevelserializer.is_valid():
            objlevelserializer.save()
            return JsonResponse(objlevelserializer.data)
        return JsonResponse(
            objlevelserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        # request.method == 'DELETE':
        objectlevelatrributeslist.delete()
        return JsonResponse(
            {'message': 'objectLevelAttribute was deleted successfully!'},
            status=status.HTTP_204_NO_CONTENT)

# writing get, put, delete, post methods for ScenelevelAtrributes


@api_view(['GET', 'POST', 'DELETE'])
def scenelevelattributes(request):
    """
    This method is add new scenelevel attributes like
    road type, tunnel etc..
    """
    if request.method == 'POST':
        obj = SceneLevel()
        obj.Light_Condition = request.data['Light_Condition']
        obj.Road_Type = request.data['Road_Type']
        obj.Road_works = request.data['Road_works']
        obj.Tunnel = request.data['Tunnel']
        obj.Weather = request.data['Weather']
        obj.Street_Condition = request.data['Street_Condition']
        obj.save()
        return Response("Saved successfully")

    if request.method == 'GET':
        getscenelevelattributes = SceneLevel.objects.all().values()
        return Response(getscenelevelattributes)

    else:
        #request.method == 'DELETE'
        count = SceneLevel.objects.all().delete()
        return JsonResponse(
            {'message': '{} scenelevelAttributes  deleted successfully!'.format(
                count[0])},
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def scenelevelattributes_id(request, p_k):
    """
    Different operations are performed on scene level attributes based on id
    """
    try:
        scenelevelatrributeslist = SceneLevel.objects.get(pk=p_k)
    except SceneLevel.DoesNotExist:
        return JsonResponse(
            {'message': 'The scenelevelAttributes does not exist'},
            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        scenelevelserializer = SceneLevelSerializer(scenelevelatrributeslist)
        return JsonResponse(scenelevelserializer.data)

    if request.method == 'PUT':
        cat_data = JSONParser().parse(request)
        print(cat_data)
        scenelevelserializer = SceneLevelSerializer(
            scenelevelatrributeslist, data=cat_data)
        if scenelevelserializer.is_valid():
            scenelevelserializer.save()
            return JsonResponse(scenelevelserializer.data)
        return JsonResponse(scenelevelserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        scenelevelatrributeslist.delete()
        return JsonResponse(
            {'message': 'scenelevelAttribute was deleted successfully!'},
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def project_files(request):
    """
    This method is to add new details of project files like
    tool version, project name and feature
    """
    if request.method == 'POST':
        obj = ProjectFiles()
        project_f = request.data['project_Feature']
        tool_v = request.data['Tool_version']
        feature_without = str(project_f)[1:-1]
        tool_without = str(tool_v)[1:-1]
        obj = ProjectFiles()  # gets new object
        obj.project_name = request.data['project_name']
        obj.project_Feature = feature_without
        obj.Tool_version = tool_without
        obj.save()
        return Response("Saved successfully")

    if request.method == 'GET':
        getprojectfilesdetails = ProjectFiles.objects.all().values()
        return Response(getprojectfilesdetails)

    else:
        #request.method == 'DELETE'
        count = ProjectFiles.objects.all().delete()
        return JsonResponse(
            {'message': '{} projets deleted successfully!'.format(count[0])},
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def projectfiles_id(request, p_k):
    """
    Different operations are performed on sceneproject files based on id
    """
    try:
        projectfileslist = ProjectFiles.objects.get(pk=p_k)
    except ProjectFiles.DoesNotExist:
        return JsonResponse(
            {'message': 'The projectFiles does not exist'},
            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        projectfileserializer = ProjectFilesSerializer(projectfileslist)
        return JsonResponse(projectfileserializer.data)

    if request.method == 'PUT':
        cat_data = JSONParser().parse(request)
        print(cat_data)
        projectfileserializer = ProjectFilesSerializer(
            projectfileslist, data=cat_data)
        if projectfileserializer.is_valid():
            projectfileserializer.save()
            return JsonResponse(projectfileserializer.data)
        return JsonResponse(projectfileserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        projectfileslist.delete()
        return JsonResponse(
            {'message': 'project was deleted successfully!'},
            status=status.HTTP_204_NO_CONTENT)


# writing get, put, delete, post methods for TaskFiles(project name, tool version, feature)
@api_view(['GET', 'POST', 'DELETE'])
def taskfiles_list(request):
    """
    This method is to add new task
    """
    if request.method == 'POST':
        obj = assignTaskFiles()
        obj.File_Name = request.data['File_Name']
        obj.project_name = request.data['project_name']
        obj.Task_level = request.data['Task_level']
        obj.Priority = request.data['Priority']
        obj.Created_Date = request.data['Created_Date']
        obj.status = request.data['status']
        obj.Action = request.data['Action']
        obj.save()
        return Response("Saved successfully")

    if request.method == 'GET':
        gettaskfilesdetails = assignTaskFiles.objects.all().values()
        return Response(gettaskfilesdetails)

    else:
        #request.method == 'DELETE'
        count = assignTaskFiles.objects.all().delete()
        return JsonResponse(
            {'message': '{} tasks were deleted successfully!'.format(
                count[0])},
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def taskfileslist_id(request, p_k):
    """
    Based on id -p_k different operations like GET, PUT, DELETE operations
    are performed
    """
    try:
        taskfileslist = assignTaskFiles.objects.get(pk=p_k)
    except assignTaskFiles.DoesNotExist:
        return JsonResponse(
            {'message': 'The task does not exist'},
            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        taskfileserializer = TaskFilesSerializer(taskfileslist)
        return JsonResponse(taskfileserializer.data)

    if request.method == 'PUT':
        cat_data = JSONParser().parse(request)
        print(cat_data)
        taskfileserializer = TaskFilesSerializer(taskfileslist, data=cat_data)
        if taskfileserializer.is_valid():
            taskfileserializer.save()
            return JsonResponse(taskfileserializer.data)
        return JsonResponse(taskfileserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        taskfileslist.delete()
        return JsonResponse(
            {'message': 'task was deleted successfully!'},
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def gettasksfilteredon_projects(request, project_name):
    """
    This method filters and return task files based on project name
    taken as argument
    """
    if request.method == 'GET':
        projectdetails = assignTaskFiles.objects.all()
        project_name = request.GET.get('project_name', None)
        print("projectfilestask", project_name)
        listing = projectdetails.filter(project_name=project_name).values()
        # print(listing)
        return Response(listing)


@api_view(['GET', 'PUT', 'DELETE'])
def getprojectdetails(request, project_name):
    """
    filters based on project name and get tool versu=ion and feature details
    of respective project
    """
    if request.method == 'GET':
        projectdetails = ProjectFiles.objects.all()
        project_name = request.GET.get('project_name', None)
        print("projectname", project_name)
        filteredlist = projectdetails.filter(
            project_name=project_name).values()
        #print("filtered list",filteredList)
        return Response(filteredlist)


@api_view(['GET', 'POST', 'DELETE'])
def getobject_categories(request):
    """
    perform different operations based on category id
    """
    if request.method == 'POST':
        obj = Objectcategories()
        obj.object_category = request.data['object_category']
        obj.save()
        return Response("Saved successfully")

    if request.method == 'GET':
        category_names = Objectcategories.objects.all().values()
        return Response(category_names)

    else:
        #request.method == 'DELETE'
        count = Objectcategories.objects.all().delete()
        return JsonResponse(
            {'message': '{} obects were deleted successfully!'.format(
                count[0])},
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def getobjectcategories_id(request, p_k):
    """
    This method is to perform different operations on category like
    'Truck','car' etc.. based on id
    here pk = id
    """
    try:
        categorynames = Objectcategories.objects.get(pk=p_k)
    except Objectcategories.DoesNotExist:
        return JsonResponse(
            {'message': 'The object does not exist'},
            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        category_serializer = ObjectcategoriesSerializer(categorynames)
        return JsonResponse(category_serializer.data)

    if request.method == 'PUT':
        cat_data = JSONParser().parse(request)
        print(cat_data)
        category_serializer = ObjectcategoriesSerializer(
            categorynames, data=cat_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse(category_serializer.data)
        return JsonResponse(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        categorynames.delete()
        return JsonResponse(
            {'message': 'object was deleted successfully!'},
            status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def uploadimages(request):
    """
    This method is add annotated image and save file name in the folder called
    annotation_images
    """
    print("request is ", request)
    title = request.POST.get('project_name')
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    obj = assignTaskFiles()
    obj.File_Name = file
    obj.project_name = title
    obj.Task_level = request.POST.get('Task_level')
    obj.Priority = request.POST.get('Priority')
    obj.Created_Date = request.POST.get('Created_Date')
    obj.status = request.POST.get('status')
    obj.Action = request.POST.get('Action')
    obj.save()
    return JsonResponse(file_name, safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
def getannotation_imagefile(request, File_Name, project_name):
    """
    This method returns image based on file name and project name
    """
    if request.method == 'GET':
        projectdetails = assignTaskFiles.objects.all()
        project_name = request.GET.get('project_name')
        File_Name = request.GET.get('File_Name')
        print("projectname", project_name)
        print("filename", File_Name)
        fetchfileandprojectname = projectdetails.filter(
            project_name=project_name, File_Name=File_Name).values()
        return Response(fetchfileandprojectname)
