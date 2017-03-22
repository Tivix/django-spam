from django.conf import settings


# common endpoints bots like
SPAM_ROUTES = [
    'admin.php',
    'admin/login.php',
    'administrator/index.php',
    'index.php',
    'wp-admin/admin-ajax.php',
    'wp-admin/post-new.php',
    'wp-admin/options-link.php',
    'wp-admin/includes/themes.php',
    'wp-login.php'
]

# '10 hours of'...
SPAM_URLS = [
    # donald trump saying bing bing bong
    'https://www.youtube.com/watch?v=UKbOqEk6rsk',
    # darth vader breathing
    'https://www.youtube.com/watch?v=un8FAjXWOBY',
    # donald trump noises
    'https://www.youtube.com/watch?v=GQPO4nmFkCI',
    # all star windows xp remix
    'https://www.youtube.com/watch?v=bKf9_gF5h5I',
    # aint nobody got time for that
    'https://www.youtube.com/watch?v=Kp9soHooisk'
]

# check if any settings vars have been included to add to the
# list of routes or urls
if hasattr(settings, 'SPAM_ROUTES'):
    SPAM_ROUTES += settings.SPAM_ROUTES

if hasattr(settings, 'SPAM_URLS'):
    SPAM_URLS += settings.SPAM_URLS
