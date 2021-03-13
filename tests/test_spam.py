import random
import sys
from io import StringIO
from importlib import reload

from django.conf import settings
from django.test import TestCase, override_settings

from django_spam import SPAM_ROUTES


class DjangoSpamTestCase(TestCase):
    def test_redirect_random_route(self):
        response = self.client.get("/" + random.choice(SPAM_ROUTES))
        self.assertEqual(response.status_code, 302)

    def test_add_spam_routes_in_settings(self):
        spam_routes = getattr(settings, "SPAM_ROUTES", [])
        response = self.client.get("/" + spam_routes[-1])
        self.assertEqual(response.status_code, 302)

    def test_excluded_routes(self):
        excluded_routes = getattr(settings, "EXCLUDED_ROUTES", [])
        response = self.client.get("/" + excluded_routes[-1])
        self.assertEqual(response.status_code, 200)

    @override_settings(
        EXCLUDED_ROUTES=[
            "notinlist.html",
        ]
    )
    def test_excluded_routes_contains_non_existent_spam_route(self):
        # create string object, redirect to stdout, reload package, then reset redirect
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        import django_spam

        reload(django_spam)
        sys.stdout = sys.__stdout__

        captured_output = capturedOutput.getvalue()
        self.assertIn("Warning:", captured_output) and self.assertIn(
            "is not included in django_spam.SPAM_ROUTES.", captured_output
        )
