from elasticsearch import serializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from authentication.api.serializers import UserSerializer


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
