from blog.api.serializers import BlogSerializer
from blog.models import Blog
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes([AllowAny])
def get_latest_posts(request):
    print('hi')
    latest = Blog.objects.order_by("-created_at")[:4]
    print(latest)

    serializer = BlogSerializer(latest, many=True)
    print('data:', serializer.data)

    return Response(serializer.data)
    # return Response(serializer.data)
