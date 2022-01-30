from . import views
from django.urls import path


# app_name = 'main_api'

urlpatterns = [
    path('get-home-posts/', views.get_home_posts,
         name="get_home_posts"),

    path('get-blog-by-category/<slug:category>/', views.get_all_posts,
         name="get_all_posts"),

    path('get-blog-by-tag/<slug:tag>/', views.get_posts_by_tag,
         name="get_posts_by_tag"),

    path('get-releted-posts-by-tag/<slug:post_slug>/', views.get_releted_posts_by_tag,
         name="get_releted_posts_by_tag"),

    path('get-post-detail/<slug:post_slug>/', views.get_post_detail,
         name="get_post_detail"),
]
