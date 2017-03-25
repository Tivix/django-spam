dj_spam
=======

We all hate bots, lets admit it. Especially the ones that try to gain access to our most secret endpoints. Well we have an easy
solution for your django application. dj_spam simply adds common admin urls to url conf so when bots (or human
for that matter) try and access them, they will get redirected...

For now, add this line to your requirements.txt file:

.. code:: python

   -e git+http://github.com/nickatnight/dj-spam.git#egg=dj-spam

Add to apps list:

.. code:: python

   INSTALLED_APPS = [
       '...',
       'dj_spam',
       '...'
   ]

dj_spam ships with some default endpoints bots might try to hit. If you would like to add extra routes, simply add
a ``SPAM_ROUTES`` variable to your settings file that contains a list of extra endpoints you would like
to add. *no leading slashes*

.. code:: python

   SPAM_ROUTES = [
       'admin.php',
       'admin/login.php',
       'administrator/index.php',
       'index.php',
       '...',
   ]

The same goes for ``SPAM_URLS`` you would like traffic to get forwarded to. Add some fun urls:

.. code:: python

   SPAM_URLS = [
       # 10 hours of Donald Trump saying bing bing bong
       'https://www.youtube.com/watch?v=UKbOqEk6rsk',
       # 10 hours of Darth Vader breathing
       'https://www.youtube.com/watch?v=un8FAjXWOBY',
       '...',
   ]

Include ``dj_spam.urls`` to root url file:

.. code:: python

   '...'
   (r'', include('dj_spam.urls')),
   '...',


If for some odd reason you need to exclude routes, define ``EXCLUDED_ROUTES`` in settings. *no leading slashes*

.. code:: python

   EXCLUDED_ROUTES = [
       'admin.php',
       'index.php'
   ]


@Tivix
