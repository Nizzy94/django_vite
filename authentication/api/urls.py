from . import views
from django.urls import path


urlpatterns = [
    path('user/', views.get_auth_user,
         name="get_auth_user"),
    path('complete-signup/', views.complete_signup,
         name="complete_signup_api"),


]
