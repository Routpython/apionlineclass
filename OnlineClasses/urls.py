"""OnlineClasses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('adlogin/',views.adlogin,name='adlogin'),
    path('newclass/',views.newclass,name='newclass'),
    path('viewallclass/',views.viewallclass,name='viewallclass'),
    path('subupdate/',views.subupdate,name='subupdate'),
    path('delete/',views.delete,name='delete'),


    path('savenew/', views.savenew, name='savenew'),
    path('studenthome/',views.studenthome,name='studenthome'),
    path('st_register/',views.st_register,name='st_register'),
    path('search/',views.search,name='search'),
    path('st_save/',views.st_save,name='st_save'),
    path('st_login/',views.st_login,name='st_login'),
    path('logins_stu/',views.logins_stu,name='logins_stu'),

    path('enroll/',views.enroll,name='enroll'),
    path('e_roll/',views.e_roll,name='e_roll'),
    path('view_enroll/',views.view_enroll,name='view_enroll'),
    path('c_delete/',views.c_delete,name='c_delete')
]
