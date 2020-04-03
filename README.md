django_spam
===========

![alt text](https://media.giphy.com/media/Mr8Gr9ejR0OpW/giphy.gif "django_spam")

Inspired by this Nick Craver tweet https://twitter.com/nick_craver/status/720062942960623616

We all hate bots, lets admit it. Especially the ones that try to gain access to our most secret endpoints. Well we have an easy
solution for your django application. django_spam simply adds common admin urls to url conf so when bots (or human
for that matter) try and access them, they will get redirected...


[![Build Status](https://travis-ci.org/nickatnight/django-spam.svg?branch=master)](https://travis-ci.org/nickatnight/django-spam)
[![Coverage Status](https://coveralls.io/repos/github/nickatnight/django-spam/badge.svg?branch=master)](https://coveralls.io/github/nickatnight/django-spam?branch=master)


|            | Django 1.8         | Django 1.9         | Django 1.10        | Django 1.11        | Django 2.0         | Django 2.1         | Django 2.2         |
| --         | --                 | --                 | --                 | --                 | --                 | --                 | --                 |
| Python 2.7 | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |                    |                    |
| Python 3.4 | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |                    |
| Python 3.5 | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Python 3.6 |                    |                    |                    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Python 3.7 |                    |                    |                    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |

To install:
```python
pip install django-spam
```

Add to apps list:
```python
INSTALLED_APPS = [
    '...',
    'django_spam',
    '...'
]
```

django_spam ships with some default endpoints bots might try to hit. If you would like to add extra routes, simply add
a ``SPAM_ROUTES`` variable to your settings file that contains a list of extra endpoints you would like
to add. *no leading slashes*
```python
SPAM_ROUTES = [
    'admin.php',
    'admin/login.php',
    'administrator/index.php',
    'index.php',
    '...',
]
```

The same goes for ``SPAM_URLS`` you would like traffic to get forwarded to. Add some fun urls:

```python
SPAM_URLS = [
    # 10 hours of Donald Trump saying bing bing bong
    'https://www.youtube.com/watch?v=UKbOqEk6rsk',
    # 10 hours of Darth Vader breathing
    'https://www.youtube.com/watch?v=un8FAjXWOBY',
    '...',
]
```

Include ``django_spam.urls`` to root url file:
```python

'...'
url(r'', include('django_spam.urls')),  # for Django >= 2.0: path('', include('django_spam.urls')),
'...',
```

If for some odd reason you need to exclude routes, define ``EXCLUDED_ROUTES`` in settings. *no leading slashes*

```python
EXCLUDED_ROUTES = [
    'admin.php',
    'index.php'
]
```

@Tivix
