dj_spam
=======

We all hate bots, lets admit it. Especially the ones that try to gain access to our most secret endpoints. Well we have an easy
solution for your django application. dj_spam simply allows you to add redirect links to whatever endpoints you choose. We've included
some special ones, 10 hours of special....

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

dj_spam ships with some default endpoints bots might try to hit. If you like to add extra routes, simply add
a ``SPAM_ROUTES`` variable to your settings file that contains a list of extra endpoints you would like
to add.

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
       'https://www.youtube.com/watch?v=UKbOqEk6rsk',
       'https://www.youtube.com/watch?v=8ZcmTl_1ER8',
       '...',
   ]

Include ``dj_spam.urls`` to root url file:

.. code:: python

   from dj_spam.urls import urlpatterns as spampatterns
   '...'
   (r'^', include(spampatterns)),
   '...',

@Tivix
