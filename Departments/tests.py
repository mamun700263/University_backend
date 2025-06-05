from datetime import date
from django.utils import timezone
from django.test import TestCase

from university.models import University
from .models import Department

import logging
logger = logging.getLogger("departments.test")

class DepartmentModelTest(TestCase):
    """🧪 Test cases for the Department model."""

    def setUp(self):
        """🔧 Setup test data for each test."""
        logger.info("🔧 Setting up test University and Department...")

        self.university = University.objects.create(
            name="Test University",
            starting_date=date(2024, 9, 1),
            established_date=timezone.now().date(),
            updated_at=timezone.now(),
        )
        logger.debug(f"🏫 University created: {self.university}")

        self.department = Department.objects.create(
            university= self.university,
            name="Computer Science",
            short_name='CS',
            created_at=date.today(),
            
        )
        logger.debug(f"🏢 Department created: {self.department}")

    def test_department_str(self):
        """✅ Test the string representation of the Department model."""
        expected_str = "Computer Science (Test University)"
        actual_str = str(self.department)

        logger.info("🧪 Testing __str__ method for Department")
        logger.debug(f"Expected: {expected_str} | Got: {actual_str}")

        self.assertEqual(actual_str, expected_str)
        logger.info("✅ Department __str__ test passed")

    def test_department_has_university(self):
        """🔗 Test that a department is correctly linked to a university."""
        university_name = self.department.university.name
        logger.info("🧪 Testing university relation on Department")
        logger.debug(f"Linked university: {university_name}")

        self.assertEqual(university_name, "Test University")
        logger.info("✅ Department is linked to the correct University")

    def test_department_has_short_name(self):
        """🔗 Test that a department is correctly assaigned a shortname."""
        short_name = self.department.short_name
        logger.info("🧪 Testing university short name")
        logger.debug(f"given short name: {short_name}")

        self.assertEqual(short_name, "CS")
        logger.info("✅ Department has short name")
    # def test_department_total_students_property(self):
    #     """📊 Test the `total_students` property returns 0 when no students exist."""
    #     logger.info("🧪 Testing total_students property on Department")
    #     self.assertEqual(self.department.total_students, 0)
    #     logger.info("✅ total_students property correctly returns 0")
