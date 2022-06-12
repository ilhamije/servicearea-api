from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser

from rest_framework.test import APIClient


class CustomUserTests(APITestCase):
    client = APIClient()

    def setUp(self):
        self.data = {
            "id": "1",
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
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().email, 'neo@domain.com')

    def test_api_list_users(self):
        url = reverse('auth:providers_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_api_can_get_a_user(self):
        user = CustomUser.objects.get()
        response = self.client.get(
            reverse('auth:providers_detail',
            kwargs={'pk': user.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, user)

    def test_api_can_update_a_user(self):
        user = CustomUser.objects.get()
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
        self.assertEqual(CustomUser.objects.get().email, 'usertest@domain.com')

    def test_api_can_delete_a_user(self):
        user = CustomUser.objects.get()
        response = self.client.delete(
            reverse('auth:providers_detail',
            kwargs={'pk': user.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CustomUser.objects.count(), 0)
