from . import views
from django.urls import path
from django.urls.conf import include

# app_name = 'main_api'

urlpatterns = [
    path('get-routes/', views.APIRootView.as_view(), name="get_routes"),
    path('contact/', views.contact, name="contact_api"),
]
