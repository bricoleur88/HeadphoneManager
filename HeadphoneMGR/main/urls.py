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


app_name = 'main'
urlpatterns= [
    path('', views.main, name='main'), 
    path('regCon/', views.regHeadphone, name='regHeadphone'),
    path('search/', include('hisdata.urls')),
    path('provide/<pk>/edit', views.provHeadphone, name='provide'),
    path('return/<pk>/edit', views.retHeadphone, name='return'),
    path('change/<pk>/change', views.changeState, name='changeState'),
    path('delete/<pk>/delete', views.delete, name='delete'),

]
