import warnings
import random

from django.conf import settings
from django.test import TestCase, override_settings

from django_spam import SPAM_ROUTES


class SimpleTestCase(TestCase):

    def setUp(self):
        pass

    def test_redirect_random_route(self):
        response = self.client.get('/'+random.choice(SPAM_ROUTES))
        self.assertEqual(response.status_code, 302)
