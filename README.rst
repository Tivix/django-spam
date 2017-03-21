dj-spam
=======

Add to apps list:

.. code:: python

   INSTALLED_APPS = [
       '...',
       'dj_spam',
       '...'
   ]

Add typical bot spam routes:

.. code:: python

   SPAM_ROUTES = [
       'admin.php',
       'admin/login.php',
       'administrator/index.php',
       'index.php',
       '...',
   ]

Add some fun urls:

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

@tivix
