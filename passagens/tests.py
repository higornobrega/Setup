from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class PassageTestCase(TestCase):
    def test_passagens_index_url_is_correct(self):
        index_url = reverse('index')
        self.assertEqual(index_url, '/')