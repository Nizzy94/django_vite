
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from authentication.api.serializers import SocialAccountProviderSerializer, UserSerializer
from rest_framework.views import APIView
# from django.views.generic import TemplateView
from allauth.account.views import EmailVerificationSentView
from authentication.views import profile_page
from allauth.socialaccount.models import SocialApp


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_auth_user(request):
    auth_user = request.user
    serializer = UserSerializer(auth_user)

    nums = (5, 2, 'gt', 2, True)

    for x in nums:
        print(x)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def complete_signup(request):
    data = request.data
    data['email'] = request.user.email
    # auth_user = request.user
    serializer = UserSerializer(request.user, data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


# class AccountRegistrationView(EmailVerificationSentView):
#     pass


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def profile_page(request):
    data = request.data

    serializer = UserSerializer(instance=request.user, data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def social_providers(request):

    social_apps = SocialApp.objects.all()
    serializer = SocialAccountProviderSerializer(social_apps, many=True)

    return Response(serializer.data)
