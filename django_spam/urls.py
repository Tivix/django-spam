import random

from django.urls import path
from django.views.generic.base import RedirectView

from django_spam import SPAM_ROUTES
from django_spam import SPAM_ENUMS


urlpatterns = list()

for spam_route in SPAM_ROUTES:
    enum = random.choice(SPAM_ENUMS)
    urlpatterns.append(
        path(
            spam_route,
            RedirectView.as_view(url=enum.url),
            name=enum.to_readable(),
        )
    )
