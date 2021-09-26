from django.conf.urls import url, include
from django.contrib import admin


try:
    from django.urls import re_path as url  # Django >= 2.0
except ImportError:
    from django.conf.urls import url  # Django < 2.0


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"", include("django_spam.urls")),
]
