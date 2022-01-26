from . import views
from django.urls import path


# app_name = 'main_api'

urlpatterns = [
    path('get-home-posts/', views.get_home_posts,
         name="get_home_posts"),

    path('get-blog-by-category/<slug:category>/', views.get_all_posts,
         name="get_all_posts"),
]
