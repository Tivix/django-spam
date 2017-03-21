from django.conf import settings


# verify user has defined necessary list in settings.
try:
    getattr(settings, SPAM_URLS)
except Exception:
    raise 'You have not defined any SPAM_URLS in your settings.'
try:
    getattr(settings, SPAM_ROUTES)
except:
    raise 'You have not defined any SPAM_ROUTES in your settings.'
