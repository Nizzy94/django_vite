
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
            'all': reverse('blog:blog', request=request),
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
            # link_name = cat.name.lower().replace(" ", "_")

            blog_cats['categories'].append({
                'name': cat.name,
                'url': reverse('blog:blog_cat', kwargs={
                    'slug': cat.slug}, request=request)
            })

            # blog_cats[link_name] = {}

            # blog_cats[link_name]['name'] = cat.name
            # blog_cats[link_name]['url'] = reverse(
            #     'blog:blog_cat', kwargs={'slug': cat.slug}, request=request)

        data = {
            'home': reverse('main:home', request=request),
            'about': reverse('main:about', request=request),
            'contact': reverse('main:contact', request=request),
            'blog': blog_cats
        }

        return Response(data)
