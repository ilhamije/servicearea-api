from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser

from rest_framework.test import APIClient


class CustomUserTests(APITestCase):
    client = APIClient()

    def setUp(self):
        admin_data = {
                "email": "admin@domain.com",
                "password": "secured-passw",
                "name":"Admin",
                "is_staff":True}

        admin_created = self.client.post(
                reverse('auth:providers_create'),
                admin_data,
                format="json")

        if admin_created.status_code==201:
            access_token = admin_created.data["access"]

        # authenticate using the token header
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {access_token}')
        self.data = {
            "id": "2",
            "name": "Tom Anderson, Inc",
            "email": "neo@domain.com",
            "phone_number": "72938190",
            "language": "English",
            "currency": "USD"
        }
        self.response = self.client.post(
            reverse('auth:providers_create'),
            self.data,
            format="json")

    def test_api_create_user(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 2)
        self.assertEqual(CustomUser.objects.last().email, 'neo@domain.com')

    def test_api_list_users(self):
        url = reverse('auth:providers_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomUser.objects.count(), 2)

    def test_api_can_get_a_user(self):
        user = CustomUser.objects.last()
        response = self.client.get(
            reverse('auth:providers_detail',
            kwargs={'pk': user.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, user)

    def test_api_can_update_a_user(self):
        user = CustomUser.objects.last()
        new_data = {
            "name": "User Test Update",
            "email": "usertest@domain.com",
            "password": "usertestpassword"
        }
        response = self.client.patch(
            reverse('auth:providers_detail',
            kwargs={'pk': user.id}), data=new_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomUser.objects.last().email, 'usertest@domain.com')

    def test_api_can_delete_a_user(self):
        user = CustomUser.objects.last()
        response = self.client.delete(
            reverse('auth:providers_detail',
            kwargs={'pk': user.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CustomUser.objects.count(), 1)
