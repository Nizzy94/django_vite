from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse
# from rest_framework.reverse import reverse
from rest_framework.views import APIView


# @api_view(["GET"])
# @permission_classes([AllowAny])
# def get_routes(request):
#     api_root = reverse_lazy('main:get_routes', request=request)
#     return Response({'me': api_root})


class APIRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = {
            'home': reverse('main:home', request=request),
            'about': reverse('main:about', request=request),
            'contact': reverse('main:contact', request=request),
        }

        return Response(data)
