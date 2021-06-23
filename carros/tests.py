from django.test import TestCase

# PRUEBA
from django.test import SimpleTestCase

class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)