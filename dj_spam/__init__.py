import warnings

from django.conf import settings
from utils import ColorMe

# verify user has defined necessary list in settings.
try:
    spam_urls = getattr(settings, 'SPAM_URLS')
except:
    raise AttributeError(ColorMe.color_text('You have not defined any SPAM_URLS in your settings.', 'fail'))

if len(spam_urls) == 0:
    warnings.warn(ColorMe.color_text('You have not added any urls for spam bots to get redirected to...please add some.', 'warn'))

try:
    spam_routes = getattr(settings, 'SPAM_ROUTES')
except:
    raise AttributeError(ColorMe.color_text('You have not defined any SPAM_ROUTES in your settings.', 'fail'))

if len(spam_routes) == 0:
    warnings.warn(ColorMe.color_text('You have not added any routes for spam bots to get redirected to...please add some.', 'warn'))
