from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ServiceArea

from rest_framework.test import APIClient


class ServiceAreaTests(APITestCase):
    client = APIClient()

    def setUp(self):
        self.data = {
            "name": "Middle Earth",
            "price": "20",
            "geojson_data": {},
            "user_id": "1"
        }
        self.response = self.client.post(
            reverse('areas:servicearea_list'),
            self.data,
            format="json")


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
