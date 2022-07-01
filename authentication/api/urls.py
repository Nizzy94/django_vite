from . import views
from django.urls import path


urlpatterns = [
    path('user/', views.get_auth_user,
         name="get_auth_user"),
    path('complete-signup/', views.complete_signup,
         name="complete_signup_api"),
    path('user/social/providers/', views.social_providers,
         name='social_providers_api'),
    path('user/profile/', views.profile_page,
         name='profile_api'),

]
