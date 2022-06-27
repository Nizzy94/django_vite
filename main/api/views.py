
from blog.models import Category
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

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
            'auth_routes': {
                'login_redirect': reverse('authentication:login_redirect', request=request),
                'account_login': reverse('account_login', request=request),
                'account_signup': reverse('account_signup', request=request),
                'login_page': reverse('authentication:login_auth', request=request),
                'signup_page': reverse('authentication:signup_auth', request=request),
                'logout_redirect': reverse('authentication:logout_redirect', request=request),
                'account_logout': reverse('account_logout', request=request),
                'profile_page': reverse('authentication:profile_page', request=request),
                # 'account_set_password': reverse('account_set_password', request=request),
                # 'account_change_password': reverse('account_change_password', request=request),
                # 'account_reset_password': reverse('account_reset_password', request=request),
                'account_email': reverse('account_email', request=request),
                # 'account_confirm_email': reverse('account_confirm_email', args=[''], request=request),
                # 'socialaccount_connections': reverse('socialaccount_connections', request=request),
                'google_login': reverse('authentication:google_login', request=request),
                'google_login_validate': reverse('authentication:google_login_validate', request=request),
            },
        }

        return Response(data)
