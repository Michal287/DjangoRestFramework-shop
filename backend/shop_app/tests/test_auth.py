from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import User
from rest_framework import status


class RegisterTests(APITestCase):
    def setUp(self):
        self.email = 'test@email.com'
        self.password = 'Pass*32word4'
        self.url = 'shop_app:register'

    def test_register(self):
        data = self.client.post(reverse(self.url), data={
            'email': self.email,
            'password': self.password,
            'password2': self.password,

        })

        self.assertEqual(data.status_code, 201)
        users = User.objects.all()
        self.assertEqual(users.count(), 1)

    def test_email_validation_register(self):
        data = self.client.post(reverse(self.url), data={
            'email': 'pass',
            'password': self.password,
            'password2': self.password,

        })

        self.assertEqual(data.status_code, 400)

    def test_password_validation_register(self):
        data = self.client.post(reverse(self.url), data={
            'email': self.email,
            'password': 'pass',
            'password2': 'pass',

        })

        self.assertEqual(data.status_code, 400)


class PasswordResetTests(APITestCase):
    def setUp(self):
        self.email = 'test@email.com'
        self.password = 'zaq1@WSX'
        self.user = User.objects.create_user(self.email, self.password)
        self.request_password_reset_url = 'shop_app:request_password_reset'
        self.password_reset_url = 'shop_app:password_reset'

    def test_request_password_reset(self):
        data = self.client.post(reverse('shop_app:request_password_reset'), data={
            'email': self.email,
        })

        self.assertEqual(data.status_code, 201)

    def test_request_password_reset_email_not_exist_validation(self):
        data = self.client.post(reverse(self.request_password_reset_url), data={
            'email': 'notexist@email.com',
        })

        self.assertEqual(data.status_code, 400)

    def test_password_reset(self):
        self.user.is_active = True
        self.user.save()

        resp = self.client.post(reverse('shop_app:login'), data={
            'email': self.email,
            'password': self.password,
        })

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        data = self.client.post(reverse(self.password_reset_url), data={
            'password': 'xsw2#EDC$',
            'password2': 'xsw2#EDC$',
            'token': resp.data['access'],
        })

        self.assertEqual(data.status_code, 201)





