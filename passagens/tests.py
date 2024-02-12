from django.test import TestCase


# Create your tests here.
class PassageTestCase(TestCase):
    def test_the_pytest_is_ok(self):
        print('Teste de passagem')
        assert 1==1