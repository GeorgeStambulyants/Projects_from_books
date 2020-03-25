from django.test import TestCase


class Test(TestCase):

    def test_right_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'shop/product/list.html')
