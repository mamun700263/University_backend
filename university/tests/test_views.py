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
            name="API University",
            established_date=date(2010, 5, 20),
        )
        self.valid_data = {
            "name": "New API University",
            "established_date": "2015-06-01"
        }

    def test_01_list_universities(self):
        url = reverse("university-list")
        logger.debug(f"[T01] Testing GET {url} — List universities")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        logger.info(f"✅ [T01] Passed. Status: {response.status_code}, Count: {len(response.data)}")

    def test_02_retrieve_university(self):
        url = reverse("university-detail", kwargs={"pk": self.uni.pk})
        logger.debug(f"[T02] Testing GET {url} — Retrieve university")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "API University")
        logger.info("✅ [T02] Passed. Retrieved name matches expected.")

    def test_03_create_university(self):
        url = reverse("university-list")
        logger.debug(f"[T03] Testing POST {url} — Create university with valid data")
        response = self.client.post(url, self.valid_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], "New API University")
        logger.info("✅ [T03] Passed. University created successfully.")

    def test_04_update_university(self):
        url = reverse("university-detail", kwargs={"pk": self.uni.pk})
        data = {
            "name": "Updated University",
            "established_date": "2020-01-01"
        }
        logger.debug(f"[T04] Testing PUT {url} — Full update")
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.uni.refresh_from_db()
        self.assertEqual(self.uni.name, "Updated University")
        logger.info("✅ [T04] Passed. University updated successfully.")

    def test_05_create_invalid_university(self):
        url = reverse("university-list")
        bad_data = {"name": "", "established_date": ""}
        logger.debug(f"[T05] Testing POST {url} — Invalid data rejection")
        response = self.client.post(url, bad_data, format='json')
        self.assertEqual(response.status_code, 400)
        logger.info("✅ [T05] Passed. Invalid data correctly rejected.")

    def test_06_partial_update_university(self):
        url = reverse("university-detail", kwargs={"pk": self.uni.pk})
        logger.debug(f"[T06] Testing PATCH {url} — Partial update")
        response = self.client.patch(url, {"name": "Partially Updated U"}, format='json')
        self.assertEqual(response.status_code, 200)
        self.uni.refresh_from_db()
        self.assertEqual(self.uni.name, "Partially Updated U")
        logger.info("✅ [T06] Passed. University name partially updated.")

    def test_07_delete_university(self):
        url = reverse("university-detail", kwargs={"pk": self.uni.pk})
        logger.debug(f"[T07] Testing DELETE {url} — Delete university")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        logger.info("✅ [T07] Passed. University deleted successfully.")

# Reference Table
# | ViewSet Method       | URL                     | Reverse Name          |
# | -------------------- | ----------------------- | --------------------- |
# | `list()`             | `/universities/`        | `"university-list"`   |
# | `retrieve(pk)`       | `/universities/<pk>/`   | `"university-detail"` |
# | `create()`           | `/universities/` (POST) | `"university-list"`   |
# | `update(pk)`         | `/universities/<pk>/`   | `"university-detail"` |
# | `partial_update(pk)` | `/universities/<pk>/`   | `"university-detail"` |
# | `destroy(pk)`        | `/universities/<pk>/`   | `"university-detail"` |
