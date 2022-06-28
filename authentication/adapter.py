# from urllib.parse import urlsplit
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account import app_settings
from allauth.account.views import get_current_site
from allauth.utils import urlsplit

from django.urls import reverse


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        site = get_current_site(request)
        location = reverse("account_confirm_email",
                           args=[emailconfirmation.key])

        bits = urlsplit(location)
        if not (bits.scheme and bits.netloc):
            uri = '{proto}://{domain}{url}'.format(
                proto=app_settings.DEFAULT_HTTP_PROTOCOL,
                domain=site.domain,
                url=location)
        else:
            uri = location

        return uri
