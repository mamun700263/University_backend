from rest_framework.test import APITestCase
from django.urls import reverse
from university.models import University
from datetime import date
import logging

logger = logging.getLogger('university.test.view')

class UniversityAPITest(APITestCase):
    def setUp(self):
        super().setUp()
        self.uni = University.objects.create(
            name="API U",
            established_date=date(2010, 5, 20),
        )
        self.valid_data = {
            "name": "New API U",
            "established_date": "2015-06-01"
        }

    def test_list_universities(self):
        logger.debug("GET /universities/ — listing universities")
        url = reverse("university-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        logger.info("✅ List API test passed.")

    def test_retrieve_university(self):
        logger.debug("GET /universities/<id>/ — retrieve single")
        url = reverse("university-detail", kwargs={"pk": self.uni.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "API U")
        logger.info("✅ Retrieve API test passed.")

    def test_create_university(self):
        logger.debug("POST /universities/ — creating")
        url = reverse("university-list")
        response = self.client.post(url, self.valid_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], "New API U")
        logger.info("✅ Create API test passed.")

    def test_update_university(self):
        logger.debug("PUT /universities/<id>/ — full update")
        url = reverse("university-detail", kwargs={"pk": self.uni.pk})
        data = {
            "name": "Updated U",
            "established_date": "2020-01-01"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.uni.refresh_from_db()
        self.assertEqual(self.uni.name, "Updated U")
        logger.info("✅ Update API test passed.")

    def test_create_invalid_university(self):
        logger.debug("POST /universities/ — invalid data test")
        url = reverse("university-list")
        bad_data = {"name": "", "established_date": ""}
        response = self.client.post(url, bad_data, format='json')
        self.assertEqual(response.status_code, 400)
        logger.info("✅ Invalid data rejection test passed.")
