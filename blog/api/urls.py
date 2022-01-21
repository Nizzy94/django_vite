from . import views
from django.urls import path


# app_name = 'main_api'

urlpatterns = [
    path('get-latest-posts/', views.get_latest_posts,
         name="get_latest_posts"),
]
