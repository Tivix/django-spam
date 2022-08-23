import random

from django.urls import path
from django.views.generic.base import RedirectView

from django_spam import SPAM_ROUTES
from django_spam import SPAM_ENUMS


def get_spam_path(route: str) -> path:
    u = random.choice(SPAM_ENUMS)
    p = path(
        route,
        RedirectView.as_view(url=u.url),
        name=u.to_readable(),
    )
    return p


urlpatterns = [get_spam_path(spam_route) for spam_route in SPAM_ROUTES]
