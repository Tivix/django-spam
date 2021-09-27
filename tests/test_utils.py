from django_spam.utils import Colour

from django.test import TestCase


class DjangoSpamUtilsTestCase(TestCase):
    """
    We use assertIn due to unicode preceding and trailing text...for
    visual clarity.
    """

    def test_fail_text(self):
        fail_text = Colour.text("Fail text.", "fail")
        self.assertIn("Fail text.", fail_text)

    def test_ok_text(self):
        ok_text = Colour.text("Ok text.", "ok")
        self.assertIn("Ok text.", ok_text)

    def test_warn_text(self):
        warn_text = Colour.text("Warn text.", "warn")
        self.assertIn("Warn text.", warn_text)

    def test_no_status_text(self):
        warn_text = Colour.text("Warn text.")  # pylint: disable=no-value-for-parameter
        self.assertIn("Warn text.", warn_text)

    def test_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            Colour()
