from django.shortcuts import redirect, render
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def login_page(request):
    next_url = request.GET.get("next", '')
    print('email_ver_redi', request.session.get(
        'email_confirmation_redirect_url'))
    request.session['redirect_url'] = next_url

    login_url = reverse('account_login')
    next_param = '?next=%s' % next_url if next_url and (next_url != reverse(
        'authentication:login_auth') or next_url != reverse('authentication:signup_auth')) else ''

    full_redirect_url = '%s%s' % (login_url, next_param)

    return HttpResponseRedirect(full_redirect_url)

    # return render(request, "authentication/login.html")


def signup_page(request):
    next_url = request.GET.get("next")
    print('next in signup_page', next_url)
    # print('next in meta', request.META.get('HTTP_REFERER'))
    request.session['redirect_url'] = next_url
    request.session['email_confirmation_redirect_url'] = next_url

    signup_url = reverse('account_signup')
    next_param = '?next=%s' % next_url if next_url and (next_url != reverse(
        'authentication:login_auth') or next_url != reverse('authentication:signup_auth')) else ''

    full_redirect_url = '%s%s' % (signup_url, next_param)

    return HttpResponseRedirect(full_redirect_url)

    # return render(request, "authentication/login.html")


@login_required
def complete_signup(request):
    return render(request, "authentication/complete-signup.html")


def login_redirect(request):
    next_url = request.session.get(
        'redirect_url') if request.session.get('redirect_url') else '/'

    if request.user.first_name == "" or request.user.last_name == "" or request.user.username == "":
        next_url = reverse("authentication:complete_signup")

    print('next in login_redirect', next_url)

    redirect_to = request.build_absolute_uri(f"{next_url}")

    return HttpResponseRedirect(redirect_to)


# @login_required
# def logout(request):

#     log_out(request)
#     next_url = request.GET.get("next", "/")
#     request.session['logout_redirect_url'] = next_url
#     return_to = urlencode(
#         {'returnTo': request.build_absolute_uri('/logout/redirect/')})
#     logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
#                  (settings.SOCIAL_AUTH_AUTH0_DOMAIN,
#                   settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
#     return HttpResponseRedirect(logout_url)


def logout_redirect(request):
    logout_redirect_url = request.GET.get("next", "/")
    # logout_redirect_url = '/'
    # print('in logout red:', request.session.get('logout_redirect_url'))
    if request.session.get('logout_redirect_url') != None:

        logout_redirect_url = request.build_absolute_uri(
            f"{request.session.get('logout_redirect_url')}")

    return HttpResponseRedirect(logout_redirect_url)


# def email_confirmation_view(request):
#     email_confirm_redirect_url = request.GET.get("next", "/")
#     # logout_redirect_url = '/'
#     print('in email-confirm view:', request.session.get('logout_redirect_url'))
#     # request.session['email_confirmation_redirect_url'] = email_confirm_redirect_url

#     return HttpResponseRedirect(email_confirm_redirect_url)


def email_confirmation_redirect(request):

    # confirmation_redirect_url = request.GET.get("next", settings.LOGIN_URL)
    confirmation_redirect_url = request.session.get(
        'email_confirmation_redirect_url'
    ) if request.session.get(
        'email_confirmation_redirect_url'
    ) else ''
    query_params = ''

    print('in logout red:', request.session.get(
        'email_confirmation_redirect_url'))

    if confirmation_redirect_url != None:
        query_params = "?next=%s" % confirmation_redirect_url if confirmation_redirect_url else ''

    full_redirect_url = '%s%s' % (reverse(settings.LOGIN_URL), query_params)

    # full_redirect_url = request.build_absolute_uri(full_redirect_link)

    return HttpResponseRedirect(full_redirect_url)


def profile_page(request):
    context = {
        'user': request.user if request.user.is_authenticated else {}
    }
    return render(request, 'authentication/profile.html', context)
