from django.conf.urls import url, include
from django.http import HttpResponse


urlpatterns = [
    url(r'', include('django_spam.urls')),
    url(r'index.php$', lambda request: HttpResponse('Hello World!')),
]
