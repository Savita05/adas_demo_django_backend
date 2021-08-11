# ADAS-ToolDemo

**Description**: This Demo application is developed to register users and login ADAS tool to add missing annotation

**Softwares integrated:**
MongoDB 
Python 3 and above version
Django 2.1.4
djangorestframework


**Flow**: 
--> Login with registered firstname and password (login credentials - firstname-admin ,pw-admin)
--> User logged in redirected to TaskListpage where user can see Taskfiles list with priority, date and status.
--> Click on start or continue will be opened to annotation page
--> On this page we can see Object level and Scene level attributes

**Commands to install and run backend server **

pip install django
pip install djangorestframework
pip install django-cors-headers
pip install djongo
python manage.py makemigrations
python manage.py migrate
pip install pylint
pip install pytest
pip install coverage
finally--
**Backend server start command**: python manage.py runserver

User can test API's working in Postman/browser using:
http://localhost:8000/registration/  --post to register new user
http://localhost:8000/getuser/ --To get registered user Details
http://localhost:8000/getTaskFilesList/ --to get List of Task files
http://localhost:8000/getObjectlevel/ -- Object level attributes
http://localhost:8000/getScenelevel/ --Scene level attributes

For swagger documentation url -http://127.0.0.1:8000/docs/

**Commands to Frontend**
After cloning/ download Github code 
Go to project folder --cd projectfolder name(ADAS-FrontEnd-main)
-- npm install
start npm server --ng serve
default port - http://localhost:4200
