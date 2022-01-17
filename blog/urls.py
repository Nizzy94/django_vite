

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name="blog"),
    path('category/<slug:slug>/', views.blog_cat, name="blog_cat"),
]
