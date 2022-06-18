from django.shortcuts import render
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def login_page(request):
    print('login_page')
    next_url = request.GET.get("next", "/")
    # print('next in login_page', next_url)
    request.session['redirect_url'] = next_url

    # login_url = '/login/auth0/'
    login_url = reverse('account_login')

    return HttpResponseRedirect(login_url)

    # return render(request, "authentication/login.html")


def signup_page(request):
    print('signup_page')
    next_url = request.GET.get("next", "/")
    # print('next in login_page', next_url)
    request.session['redirect_url'] = next_url

    # login_url = '/login/auth0/'
    signup_url = reverse('account_signup')

    return HttpResponseRedirect(signup_url)

    # return render(request, "authentication/login.html")


@login_required
def complete_signup(request):
    return render(request, "authentication/complete-signup.html")


def login_redirect(request):
    print('login_redirect')
    next_url = request.session.get('redirect_url')

    if request.user.first_name == "" or request.user.last_name == "" or request.user.username == "":
        next_url = reverse("authentication:complete_signup")

    print('next in login_redirect', next_url)

    redirect_to = request.build_absolute_uri(f"{next_url}")

    return HttpResponseRedirect(redirect_to)


@login_required
def logout(request):

    log_out(request)
    next_url = request.GET.get("next", "/")
    request.session['logout_redirect_url'] = next_url
    return_to = urlencode(
        {'returnTo': request.build_absolute_uri('/logout/redirect/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN,
                  settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)


def logout_redirect(request):
    logout_redirect_url = request.GET.get("next", "/")
    # logout_redirect_url = '/'
    # print('in logout red:', request.session.get('logout_redirect_url'))
    if request.session.get('logout_redirect_url') != None:

        logout_redirect_url = request.build_absolute_uri(
            f"{request.session.get('logout_redirect_url')}")

    return HttpResponseRedirect(logout_redirect_url)
