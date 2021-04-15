"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.homepg,name='homepg'),
    path('ananyapg',index.ananyapg, name='ananyapg'),
    path('vaibhavpg',index.vaibhavpg, name='vaibhavpg'),
    path('pravinpg',index.pravinpg, name='pravinpg'),
    path('buzzinga',index.buzzinga, name='buzzinga'),
    path('signupforms',index.signupforms, name='signupforms'),
    path('team',index.team, name='team'),
    path('tictac',index.tictac, name='tictac'),
    path('blogwrite',index.blogwrite, name='blogwrite'),
    path('after',index.after, name='after'),
    path('tileslide',index.tileslide, name='tileslide'),
    path('services',index.services, name='services'),
    path('loginform',index.loginform, name='loginform'),
    path('games',index.games, name='games'),
    path('contact',index.contact, name='contact'),
    
    
    
    
    
]