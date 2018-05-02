from __future__ import absolute_import

from django.conf import settings
from django.conf.urls import url

from django_spam import SPAM_ROUTES
from django_spam.views import ten_hours


def get_spam_urls():
    spam_urls = []
    for route in SPAM_ROUTES:
        spam_urls.append(url(r'^'+route+'$', ten_hours))

    return spam_urls


urlpatterns = get_spam_urls()
