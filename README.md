django-spam
===========

<p align="center">
<a href="https://github.com/Tivix/django-spam"><img alt="Build Status" src="https://github.com/Tivix/django-spam/workflows/lint%20and%20test/badge.svg?branch=master"></a>
<a href="https://codecov.io/gh/Tivix/django-spam"><img alt="Actions Status" src="https://codecov.io/gh/Tivix/django-spam/branch/master/graph/badge.svg"></a>
<a href="https://github.com/Tivix/django-spam/releases"><img alt="Release Status" src="https://img.shields.io/github/v/release/Tivix/django-spam"></a>
</p>

<p align="center">
<a href="https://media.giphy.com/media/Mr8Gr9ejR0OpW/giphy.gif"><img alt="spam" src="https://media.giphy.com/media/Mr8Gr9ejR0OpW/giphy.gif"></a>
</p>

Inspired by this Nick Craver tweet https://twitter.com/nick_craver/status/720062942960623616

We all hate bots, lets admit it. Especially the ones that try to gain access to our most secret endpoints. Well we have an easy
solution for your django application. django_spam simply adds common admin urls to url conf so when bots (or human
for that matter) try and access them, they will get redirected...


|            | Django 2.0         | Django 2.1         | Django 2.2         | Django 3.0         | Django 3.1         | Django 3.2         |
| --         | --                 | --                 | --                 | --                 | --                 | --                 |
| Python 3.4 | :heavy_check_mark: |                    |                    |                    |                    |                    |
| Python 3.5 | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |                    |                    |
| Python 3.6 | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Python 3.7 | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Python 3.8 |                    |                    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Python 3.9 |                    |                    |                    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |


## Installation / Usage
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

Include ``django_spam.urls`` to root url file:
```python

'...'
path('', include('django_spam.urls')),
'...',
```

If for some odd reason you need to exclude routes, define ``EXCLUDED_ROUTES`` in settings. *no leading slashes*

```python
EXCLUDED_ROUTES = [
    'admin.php',
    'index.php'
]
```

## Demo
See [here](demo/README.md)

## Development
TODO
