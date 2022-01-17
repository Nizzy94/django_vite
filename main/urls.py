
from django.urls import path
from django.urls.conf import include
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

    path('api/', include('main.api.urls')),
]
