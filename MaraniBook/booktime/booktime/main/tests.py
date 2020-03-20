from django.test import TestCase


class TestPage(TestCase):

    def test_home_page_works(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'BookTime')
