import logging
from datetime import date
from django.test import TestCase
from django.utils import timezone
from .models import University
from .serializers import UniversitySerializer

# Logger for university test suite
logger = logging.getLogger("university.tests")


class BaseUniversityTest(TestCase):
    """
    Base test case providing a shared University instance setup
    for all University-related test classes.
    """

    def setUp(self):
        """
        Creates a default University instance for use in all child test cases.
        """
        self.university = University.objects.create(
            name="Test University",
            starting_date=date(2024, 9, 1),
            established_date=timezone.now().date(),  # Ensures type-safe date
            updated_at=timezone.now(),
        )
        logger.info(f"University instance created for {self.__class__.__name__}")


class UniversityModelTest(BaseUniversityTest):
    """
    Test suite for University model field behaviors and dunder methods.
    """

    def test_university_name(self):
        """
        Verifies that the university name is stored and retrieved correctly.
        """
        logger.debug("Testing university name field...")
        self.assertEqual(self.university.name, "Test University")
        logger.info("✅ University name test passed.")

    def test_created_at_timestamp(self):
        """
        Ensures that the established_date is automatically set and not null.
        """
        logger.debug("Testing established_date field...")
        self.assertIsNotNone(self.university.established_date)
        logger.info("✅ Established date test passed.")

    def test_str_method(self):
        """
        Tests the __str__ method returns the university name.
        """
        logger.debug("Testing __str__ method...")
        self.assertEqual(str(self.university), "Test University")
        logger.info("✅ __str__ method test passed.")


class UniversitySerializerTestCase(BaseUniversityTest):
    """
    Test suite for validating serialization and data integrity
    of the University model using UniversitySerializer.
    """

    def test_serialization(self):
        """
        Tests serialization of a University instance and its updates.
        - Checks correct serialization output.
        - Verifies changes are reflected after saving and re-serializing.
        """
        logger.debug("Testing serialization (initial)...")
        serializer = UniversitySerializer(self.university)
        self.assertEqual(serializer.data["name"], "Test University")
        logger.info("✅ Initial serialization test passed.")

        logger.debug("Testing serialization (after update)...")
        self.university.name = "Update University"
        self.university.save()
        serializer = UniversitySerializer(self.university)
        self.assertEqual(serializer.data["name"], "Update University")
        logger.info("✅ Updated serialization test passed.")
