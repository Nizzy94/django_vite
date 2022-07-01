
from django.conf import settings
from blog.api.serializers import SubscriptionSerializer
from blog.models import Category
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import get_template

from main.api.serializers import ContactMessageSerializer, SocialIconsSerializer
from main.models import SocialIcon

# @api_view(["GET"])
# @permission_classes([AllowAny])
# def get_routes(request):
#     api_root = reverse_lazy('main:get_routes', request=request)
#     return Response({'me': api_root})


class APIRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        categories = Category.objects.order_by('name')
        blog_routes = {
            'all': reverse('blog:blogs', request=request),
            'categories': [],
            'subscribe': reverse('blog:subscribe', request=request)
        }

        """
        blog_routes = {
            cat_one: {
                name: cat.name    
                url: reverse('blog:blog_cat', kwargs={'slug': cat.slug}, request=request)
            }
        }
        """

        for cat in categories:

            blog_routes['categories'].append({
                'name': cat.name,
                'url': reverse('blog:blogs_cat', kwargs={
                    'category': cat.slug}, request=request)
            })

        # print(reverse('account_reset_password_from_key'))

        data = {
            'home': reverse('main:home', request=request),
            'about': reverse('main:about', request=request),
            'contact': reverse('main:contact', request=request),
            'contact_api': reverse('main:contact_api', request=request),
            'search': reverse('search:search_view', request=request),
            'blog': blog_routes,
            'auth_routes': {
                'login_redirect': reverse('authentication:login_redirect', request=request),
                'account_login': reverse('account_login', request=request),
                'login_page': reverse('authentication:login_auth', request=request),
                'rest_login': reverse('rest_login', request=request),

                'account_signup': reverse('account_signup', request=request),
                'signup_page': reverse('authentication:signup_auth', request=request),

                'logout_redirect': reverse('authentication:logout_redirect', request=request),
                'rest_logout': reverse('rest_logout', request=request),
                'account_logout': reverse('account_logout', request=request),

                'profile_page': reverse('authentication:profile_page', request=request),
                'profile_api': reverse('authentication:profile_api', request=request),
                'rest_user_details': reverse('rest_user_details', request=request),

                'account_change_password': reverse('account_change_password', request=request),
                'account_set_password': reverse('account_set_password', request=request),
                'account_reset_password': reverse('account_reset_password', request=request),


                'account_email': reverse('account_email', request=request),
                # 'account_confirm_email': reverse('account_confirm_email', args=[''], request=request),

                'socialaccount_connections': reverse('socialaccount_connections', request=request),
                'social_account_list': reverse('social_account_list', request=request),
                # 'social_account_disconnect': reverse('social_account_disconnect', request=request),
                'social_icon_api': reverse('main:social_icon_api', request=request),
                'social_providers_api': reverse('authentication:social_providers_api', request=request),
                'google_login': reverse('authentication:google_login', request=request),
                'google_connect': reverse('authentication:google_connect', request=request),
            },
        }

        return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def contact(request):
    data = request.data
    print(data)

    serializer = ContactMessageSerializer(data=data)

    # plaintext_template = get_template('blog/emails/subscription.txt')
    # html_template = get_template('blog/emails/subscription.html')
    subject, from_email, to = data['subject'],  data['email'], 'to@example.com',

    if serializer.is_valid(raise_exception=True):
        # print(serializer.validated_data)
        serializer.save()

        send_mail(
            '%s (from: %s)' % (subject, data['name']),
            data['message'],
            from_email,
            [to]
        )

        return Response({'message': 'contact message sent'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def social_icons(request):
    icons = SocialIcon.objects.all()

    serializer = SocialIconsSerializer(icons, many=True)

    return Response(serializer.data)
    # if serializer.is_valid(raise_exception=True):
