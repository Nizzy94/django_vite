
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse
# from rest_framework.reverse import reverse
from rest_framework.views import APIView

from blog.models import Category


# @api_view(["GET"])
# @permission_classes([AllowAny])
# def get_routes(request):
#     api_root = reverse_lazy('main:get_routes', request=request)
#     return Response({'me': api_root})


class APIRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        categories = Category.objects.order_by('name')
        blog_cats = {
            'all': reverse('blog:blogs', request=request),
            'categories': []
        }

        """
        blog_cats = {
            cat_one: {
                name: cat.name    
                url: reverse('blog:blog_cat', kwargs={'slug': cat.slug}, request=request)
            }
        }
        """

        for cat in categories:

            blog_cats['categories'].append({
                'name': cat.name,
                'url': reverse('blog:blogs_cat', kwargs={
                    'category': cat.slug}, request=request)
            })

        data = {
            'home': reverse('main:home', request=request),
            'about': reverse('main:about', request=request),
            'contact': reverse('main:contact', request=request),
            'search': reverse('search:search_view', request=request),
            'blog': blog_cats,
            'login_redirect': reverse('authentication:login_redirect', request=request),
        }

        return Response(data)
