from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
]
