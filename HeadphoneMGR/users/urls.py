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
"""
from django.urls import path, include, re_path
from . import views    # 어떤 것으로 들어오던 views로 

# 실질적으로 headphones에서 사용할 urls 패턴들만 관리하기위해.. 

app_name = 'users'
urlpatterns= [
    path('reg/', views.regUser, name='reg'), # url이 users/reg 로 들어왔을 때 regUser 함수 (view에서 만들어야하는)를 실행한다
]