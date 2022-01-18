

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('category/<slug:category>/', views.blogs_cat, name="blogs_cat"),
    path('category/<slug:category>/<slug:blog_slug>/',
         views.blog, name="blog_detail"),
]
