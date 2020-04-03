from django.conf import settings

from django_spam.utils import Colour


# common endpoints bots like (w/o leading slash)
SPAM_ROUTES = [
    # asp/x
    'admin.aspx',
    'admin.asp',
    'admin/account.html',
    'admin/login.asp',
    'admin_login.asp',
    'admin_login.aspx',
    'administartorlogin.aspx',
    'administrator_login.asp',
    'administrator_login.aspx',
    'login/administrator.aspx',
    'login/admin.asp',

    # php
    'admin.php',
    'admin/login.php',
    'admin_area/index.php',
    'administrator/index.php',
    'index.php',
    'siteadmin/index.php',
    'siteadmin/login.php',
    'wp-admin/admin-ajax.php',
    'wp-admin/post-new.php',
    'wp-admin/options-link.php',
    'wp-admin/includes/themes.php',
    'wp-login.php',

    # html
    'admin/account.html',
    'admin/admin.html',
    'admin/index.html',
    'admin/login.html'
]

# '10 hours of'...
SPAM_URLS = [
    # darth vader breathing
    'https://www.youtube.com/watch?v=un8FAjXWOBY',
    # yodelling
    'https://www.youtube.com/watch?v=Lxt0_YrQs0M',
    # whistling mullet guy
    'https://www.youtube.com/watch?v=Sbhoym9yzVQ',
    # screaming guy
    'https://www.youtube.com/watch?v=CRcYlE3i_-4',
    # awesome face song
    'https://www.youtube.com/watch?v=WNeni1lbzgY',
    # screaming sheep
    'https://www.youtube.com/watch?v=SjHUb7NSrNk',
    # epic sax guy
    'https://www.youtube.com/watch?v=kxopViU98Xo',
    # crab rave
    'https://www.youtube.com/watch?v=-50NdPawLVY',
    # wii theme music
    'https://www.youtube.com/watch?v=Twi92KYddW4',
    # nyan cat
    'https://www.youtube.com/watch?v=wZZ7oFKsKzY'
]

# check if any settings vars have been included to add to the
# list of routes or urls
if hasattr(settings, 'SPAM_ROUTES'):
    SPAM_ROUTES += settings.SPAM_ROUTES


# check for excluded routes
if hasattr(settings, 'EXCLUDED_ROUTES'):
    for route in settings.EXCLUDED_ROUTES:
        if route in SPAM_ROUTES:
            SPAM_ROUTES.remove(route)
        else:
            print(Colour.text('Warning: "'+ route +'" is not included in django_spam.SPAM_ROUTES.', 'warn'))


if hasattr(settings, 'SPAM_URLS'):
    SPAM_URLS += settings.SPAM_URLS
