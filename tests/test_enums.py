from django_spam.enums import SpamBase

from django.conf import settings
from django.test import TestCase


class DjangoSpamEnumsTestCase(TestCase):
    def test_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            SpamBase()
