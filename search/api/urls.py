from . import views
from django.urls import path


# app_name = 'main_api'

urlpatterns = [
    path('query/<str:query>/', views.search,
         name="search"),


]
