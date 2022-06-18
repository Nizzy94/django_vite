
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'authentication'


urlpatterns = [
    path('login/auth/', views.login_page, name="login_auth"),
    path('signup/auth/', views.signup_page, name="signup_auth"),
    path('login/redirect/', views.login_redirect, name="login_redirect"),
    path('logout/auth/', views.logout, name="logout_auth"),
    path('logout/redirect/',
         views.logout_redirect, name="logout_redirect"),
    path('complete-signup/',
         views.complete_signup, name="complete_signup"),
    path('auth/api/',
         include('authentication.api.urls')),
]
