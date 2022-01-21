

from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('api/', include('blog.api.urls')),
    path('', views.blogs, name="blogs"),
    path('<slug:category>/', views.blogs_cat, name="blogs_cat"),
    path('<slug:category>/<slug:blog_slug>/',
         views.blog, name="blog_detail"),

]
