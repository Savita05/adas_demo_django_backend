"""
This file is to register all the urls for createuser API
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
# from rest_framework.schemas import get_schema_view
# from django.urls import path
from createuser.views import Getuser, Login
from createuser import views



urlpatterns = [
url(r'registerUsers/$', views.register_users , name="register"),
url(r'registerUsers_id/(?P<p_k>[0-9]+)$', views.registerdusers_id , name = 'regid'),
#path('registerUsers_id/<int:p_k>/', views.registerdusers_id , name = 'regid'),

url(r'getuser/$', Getuser.as_view(), name="getresgisterdusers"),
url(r'loginuser/$', Login.as_view(), name="login"),

url(r'taskfilesAttributes/$', views.taskfiles_list , name = "tasks"),
url(r'taskfilesAttributes_id/(?P<p_k>[0-9]+)$', views.taskfileslist_id , name="taskid" ),
url(r'gettaskfilesfilteredonprojects/(?P<project_name>)$', views.gettasksfilteredon_projects),

url(r'objectLevelAttributes/$', views.objectlevelattributes,  name ="objectLevel"),
url(r'objectLevelAttributes_id/(?P<p_k>[0-9]+)$', views.objectlevelattributes_id, name ="objectlid"),

url(r'sceneLevelAtrributes/$', views.scenelevelattributes, name = "sceneLevel"),
url(r'sceneLevelAttributes_id/(?P<p_k>[0-9]+)$', views.scenelevelattributes_id, name="scenelevelid"),

url(r'projectFiles/$', views.project_files, name="project"),
url(r'projectFiles_id/(?P<p_k>[0-9]+)$', views.projectfiles_id, name="projectid"),

url(r'getProjectFilesname/$', views.getproject_name),
url(r'getProjectFilesdetails/(?P<project_name>)$',views.getprojectdetails),

url(r'objectCategories/$', views.getobject_categories, name ="objcat"),
url(r'objectcategorieswithid/(?P<p_k>[0-9]+)$', views.getobjectcategories_id, name ="objcatid"),

url(r'getAnnotationImageFile/(?P<File_Name>)(?P<project_name>)$', views.getannotation_imagefile),
url(r'uploadAnnotationimages/', views.uploadimages)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
