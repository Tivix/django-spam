import warnings

from django.conf import settings

from utils import ColorMe


spam_vars = ['SPAM_URLS', 'SPAM_ROUTES']

for spam_var in spam_vars:
    # verify user has defined necessary lists in settings.
    try:
        settings_val = getattr(settings, spam_var)
    except:
        raise AttributeError(ColorMe.color_text('You have not defined any ' + spam_var + ' in your settings.', 'fail'))

    if len(settings_val) == 0:
        raise ValueError(
            ColorMe.color_text(
                'You have not added any ' + spam_var[5:].lower() + ' for spam bots to get redirected to/from...please add some.',
                'warn'
            )
        )
