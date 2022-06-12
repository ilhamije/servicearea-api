from os import access
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import ServiceArea
from authentication.models import CustomUser
import requests

class ServiceAreaTests(APITestCase):

    client = APIClient()

    # data = {"name":"The Company", "email": "cs@domain.com", "password": "sembarangan"}
    # user_created = client.post(
    #         reverse('auth:providers'),
    #         data,
    #         format="json")
    # print('user_created:', user_created)

    # resp = client.post("/token/obtain", data=data)
    # access_token = resp.data["access"]
    # refresh_token = resp.data["refresh"]

    def setUp(self):
        # instance = CustomUser.objects.filter(email='pro1@domain.com')
        # if instance:
        #     instance.delete()

        # user_data = {
        #     "name": "Provider One",
        #     "email": "pro1@domain.com",
        #     "password": "some-passw"
        # }

        # user_created = requests.post('http://localhost:8000/providers', data=user_data)
        # access_token = None
        # if user_created.status_code==201:
        #     access_token = user_created.data["access"]
        #     self.client.credentials(HTTP_AUTHORIZATION=f'JWT {access_token}')

        data = {
            "name": "Middle Earth",
            "price": "20",
            "geojson_data": {},
            "user_id": 1
        }

        # authenticate using the token header
        response = self.client.post(
            reverse('areas:servicearea_list'),
            data,
            format="json")
        print(response.data)


    def test_api_create_area(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceArea.objects.count(), 1)
        self.assertEqual(ServiceArea.objects.get().name, 'Middle Earth')

    # def test_api_list_area(self):
    #     url = reverse('areas:servicearea_list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(ServiceArea.objects.count(), 1)

    # def test_api_can_get_area(self):
    #     area = ServiceArea.objects.get()
    #     response = self.client.get(
    #         reverse('areas:servicearea_detail',
    #         kwargs={'pk': area.id}), format="json"
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertContains(response, area)

    # def test_api_can_update_area(self):
    #     area = ServiceArea.objects.get()
    #     new_data = {
    #         "name": "Far Middle Earth",
    #         "price": "20",
    #         "geojson_data": {}
    #     }
    #     response = self.client.patch(
    #         reverse('areas:servicearea_detail',
    #         kwargs={'pk': area.id}), data=new_data, format="json"
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(ServiceArea.objects.get().name, 'FarMiddle Earth')

    # def test_api_can_delete_a_user(self):
    #     user = ServiceArea.objects.get()
    #     response = self.client.delete(
    #         reverse('areas:servicearea_detail',
    #         kwargs={'pk': user.id}), format="json"
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(ServiceArea.objects.count(), 0)
