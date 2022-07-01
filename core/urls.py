
from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from dj_rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)
from allauth.account.views import EmailVerificationSentView, ConfirmEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    re_path(r"^user/registration/account-confirm-email/(?P<key>[\s\d\w().+-_',:&]+)/$", ConfirmEmailView.as_view(),
            name="account_confirm_email"),
    path(
        'user/registration/account-email-verification-sent/', EmailVerificationSentView.as_view(),
        name='account_email_verification_sent',
    ),
    path('user/', include('dj_rest_auth.urls')),
    path(
        'user/socialaccounts/<int:pk>/disconnect/',
        SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'
    ),
    path(
        'user/socialaccounts/',
        SocialAccountListView.as_view(),
        name='social_account_list'
    ),
    path('user/registration/', include('dj_rest_auth.registration.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('main.urls', namespace="main")),
    path('blog/', include('blog.urls', namespace="blog")),
    path('search/', include('search.urls', namespace="search")),
    path('', include('authentication.urls', namespace="authentication")),
    # path('', include('django.contrib.auth.urls')),
    # path('', include('social_django.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
