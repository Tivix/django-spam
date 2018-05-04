from __future__ import absolute_import

from django.conf import settings
try:
    from django.urls import re_path as url  # Django >= 2.0
except ImportError:
    from django.conf.urls import url     # Django < 2.0

from django_spam import SPAM_ROUTES
from django_spam.views import ten_hours


urlpatterns = [url(r'^'+sp+'$', ten_hours) for sp in SPAM_ROUTES]
