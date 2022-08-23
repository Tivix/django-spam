from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="default_urlconf.html")),
    path("", include("django_spam.urls")),
]
