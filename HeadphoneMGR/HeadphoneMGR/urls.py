"""HeadphoneMGR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
    
    urlpatterns.. 처음프로젝트 만들면 app 마다 만들어줘도 지금의 urls.py에서만 찾음 app 쪽의 urls.py로 연결 걸어주는게 필요
    1. use 'include'
"""
from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns= [
    path('admin/', admin.site.urls),
    path('headphones/', include('headphones.urls')),  # go to urls.py in the headphones app folder
    path('users/', include('users.urls'))             # go to urls.py in the users app folder
    
]
