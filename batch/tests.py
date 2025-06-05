from django.test import TestCase
from university.models import University
from Departments.models import Department
from .models import Batch
from datetime import date
from django.utils import timezone
from django.db import IntegrityError
import logging

logger = logging.getLogger("batch.test")

class BatchModelTest(TestCase):
    """
    Test cases for the Batch model.
    """

    def setUp(self):
        # Create University
        self.university = University.objects.create(
            name="Test University",
            starting_date=date(2024, 9, 1),
            established_date=timezone.now().date(),
            updated_at=timezone.now()
        )

        # Create Department
        self.department = Department.objects.create(
            university=self.university,
            name="Computer Science",
            created_at=timezone.now().date()
        )

    def test_batch_creation_and_end_date(self):
        """
        Should correctly create a Batch and auto-set end_date = start_date + 4 years
        """
        batch = Batch.objects.create(
            department=self.department,
            batch_number=101,
            start_date=date(2020, 1, 1),
            total_students=30
        )

        expected_end_date = date(2024, 1, 1)  # 4 years later
        self.assertEqual(batch.end_date, expected_end_date)
        self.assertEqual(batch.total_students, 30)
        logger.debug(f"Batch end date correctly set to {batch.end_date}")

    def test_batch_str_method(self):
        """
        Should return correct string representation.
        """
        batch = Batch.objects.create(
            department=self.department,
            batch_number=102,
            start_date=date(2021, 9, 1),
            total_students=25
        )
        self.assertEqual(str(batch), "Batch 102 (Computer Science)")

    def test_batch_unique_constraint(self):
        """
        Should raise IntegrityError for duplicate batch_number in same department.
        """
        Batch.objects.create(
            department=self.department,
            batch_number=103,
            start_date=date(2022, 1, 1),
            total_students=40
        )

        with self.assertRaises(IntegrityError):
            Batch.objects.create(
                department=self.department,
                batch_number=103,  # Duplicate
                start_date=date(2023, 1, 1),
                total_students=50
            )

    def test_batch_number_can_repeat_in_different_department(self):
        """
        Same batch_number should be allowed in different departments.
        """
        # Create another department
        new_department = Department.objects.create(
            university=self.university,
            name="Electrical Engineering",
            created_at=timezone.now().date()
        )

        Batch.objects.create(
            department=self.department,
            batch_number=104,
            start_date=date(2023, 1, 1),
            total_students=35
        )

        try:
            Batch.objects.create(
                department=new_department,
                batch_number=104,  # Same batch_number, different dept — should work
                start_date=date(2023, 1, 1),
                total_students=40
            )
        except IntegrityError:
            self.fail("Batch number should be unique per department, not globally.")
