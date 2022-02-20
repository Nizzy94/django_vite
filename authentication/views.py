from django.shortcuts import render
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required


def login_page(request):
    # print(request.META.get('HTTP_REFERER'))
    next_url = request.GET.get("next", "/")
    request.session['redirect_url'] = next_url

    login_url = '/login/auth0/'

    return HttpResponseRedirect(login_url)

    # return render(request, "authentication/login.html")


def login_redirect(request):
    print(request.session.get('redirect_url'))
    redirect_to = request.build_absolute_uri(
        f"{request.session.get( 'redirect_url')}")

    return HttpResponseRedirect(redirect_to)


@login_required
def logout(request,):

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
    logout_redirect_url = '/'
    print('in logout red:', request.session.get('logout_redirect_url'))
    if request.session.get('logout_redirect_url') != None:

        logout_redirect_url = request.build_absolute_uri(
            f"{request.session.get('logout_redirect_url')}")

    return HttpResponseRedirect(logout_redirect_url)
