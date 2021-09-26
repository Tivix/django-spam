from django.urls import path, include
from django.http import HttpResponse


urlpatterns = [
    path("", include("django_spam.urls")),
    path("index.php", lambda request: HttpResponse("Hello World!")),
]
