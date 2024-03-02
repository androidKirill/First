from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

class IndexTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse("index_url"))
    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_simple_context(self):
        self.assertEqual(self.response.context["pages"], 1)

class CalcTest(TestCase):
    fixtures = [
        'test_database.json'
    ]

    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.get(username='vasya')
        self.client.force_login(self.user)
        self.response = self.client.get(reverse('calc_url'))

    def test_not_auth_response(self):
        c = Client()
        response = c.get(reverse('calc_url'))
        self.assertEqual(response.status_code, 302)

    def test_auth_response(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTrue('form' in self.response.context)

    def test_invalid_post(self):
        response = self.client.post(reverse('calc_url'), {'first': 'ahaha', 'second': 'ehehe'})
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.context['form'].errors), 0)
        self.assertFormError(response, 'form', 'first', 'Enter a whole number.')

