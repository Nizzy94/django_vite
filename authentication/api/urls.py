from . import views
from django.urls import path


urlpatterns = [
    path('user/', views.get_auth_user,
         name="get_auth_user"),
    path('complete-signup/', views.complete_signup,
         name="complete_signup_api"),
    path('user/google/validate/', views.GoogleLoginValidate.as_view(),
         name='google_login_validate'),
    #     path('user/google/validate/', views.googleLoginValidate,
    #          name='google_login_validate'),

]
