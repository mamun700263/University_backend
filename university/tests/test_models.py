from django.test import TestCase
from university.models import University
from datetime import date
import logging
from .base import BaseUniversityTest

from django.utils import timezone
logger = logging.getLogger('university.test.models')



class UniversityModelTest(BaseUniversityTest):
    """
    Test suite for University model field behaviors and dunder methods.
    """
    def setUp(self):
        self.university = University.objects.create(
            name="Test University",
            starting_date=date(2024, 9, 1),
            established_date=timezone.now().date(),
            updated_at=timezone.now(),
        )
        logger.info("🧪 [%s] University test instance created: %s", self.__class__.__name__, self.university.name)

    def test_university_name(self):
        logger.debug("🔍 Testing university name field...")
        self.assertEqual(self.university.name, "Test University")
        logger.info("✅ University name test passed.")

    def test_created_at_timestamp(self):
        logger.debug("🔍 Testing established_date field...")
        self.assertIsNotNone(self.university.established_date)
        logger.info("✅ Established date test passed.")

    def test_str_method(self):
        logger.debug("🔍 Testing __str__ method...")
        self.assertEqual(str(self.university), "Test University")
        logger.info("✅ __str__ method test passed.")

