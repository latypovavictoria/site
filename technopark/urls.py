"""technopark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from app import views
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('',views.like),
    path('ask/',views.ask,name='ask'),
    path('askqw/', views.askqw, name='askqw'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('settings/', views.settings, name='settings'),
    path('tags/', views.tags, name='tags'),
    path('articles/',views.articles, name='articles'),
    path('question/',views.question),
    path('like/',views.like),
]
