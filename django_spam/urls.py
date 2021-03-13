import random

from django.conf import settings
from django.urls import path
from django.views.generic.base import RedirectView

from django_spam import SPAM_ROUTES, SPAM_URLS


spam_url = random.choice(SPAM_URLS)

urlpatterns = [
    path(
        spam_route,
        RedirectView.as_view(url=spam_url.url),
        name=spam_url.to_readable(),
    )
    for spam_route in SPAM_ROUTES
]
