import random

from django.urls import path
from django.views.generic.base import RedirectView

from django_spam import SPAM_ROUTES
from django_spam import SPAM_ENUMS


spam_url = random.choice(SPAM_ENUMS)

urlpatterns = [
    path(
        spam_route,
        RedirectView.as_view(url=spam_url.url),
        name=spam_url.to_readable(),
    )
    for spam_route in SPAM_ROUTES
]
