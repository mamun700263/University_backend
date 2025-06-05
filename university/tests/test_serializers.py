from rest_framework.test import APITestCase
from university.models import University
from university.serializers import UniversitySerializer
from datetime import date
import logging
from .base import BaseUniversityTest
logger = logging.getLogger('university.test.serializers')


class UniversitySerializerTestCase(BaseUniversityTest):
    """
    Test suite for validating serialization and data integrity
    of the University model using UniversitySerializer.
    """

    def test_serialization(self):
        logger.debug("🔄 Testing serialization (initial)...")
        serializer = UniversitySerializer(self.university)
        self.assertEqual(serializer.data["name"], "Test University")
        logger.info("✅ Initial serialization test passed.")

        logger.debug("✏️ Testing serialization (after update)...")
        self.university.name = "Update University"
        self.university.save()
        serializer = UniversitySerializer(self.university)
        self.assertEqual(serializer.data["name"], "Update University")
        logger.info("✅ Updated serialization test passed.")

