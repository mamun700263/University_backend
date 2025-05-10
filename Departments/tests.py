from datetime import date

from django.test import TestCase
from university.models import University

from .models import Batch, Department


class DepartmentModelTest(TestCase):
    """Test cases for the Department model."""

    def setUp(self):
        # Create test data
        self.university = University.objects.create(
            name="Test University", created_at=date(2000, 1, 1)
        )
        self.department = Department.objects.create(
            name="Computer Science",
            # university=self.university,
            # department_head=self.teacher,
            total_students=0,
            created_at=date.today(),
        )
        print(self.department)

    def test_department_str(self):
        """Test the string representation of the Department model."""
        self.assertEqual(
            str(self.department),
            "Computer Science (Test University)"
            )
        print("hello world")
        print(self.department)

    def test_department_has_university(self):
        """Test that a department is correctly linked to a university."""
        self.assertEqual(self.department.university.name, "Test University")

    def test_department_total_students_property(self):
        """Test the `total_students` property
        returns 0 when no students exist."""
        # Assuming related_name='students' on Student model
        self.assertEqual(self.department.total_students, 0)


class Batch_Model_Test(TestCase):
    """
    Test cases for the Batch Model
    """

    # Create Test data
    def setUp(self):
        # Create a University First
        self.university = University.objects.create(
            name="Test University",
            created_at=date(2000, 1, 1),
        )

        # create a department
        self.department = Department.objects.create(
            name="Cse",
            university=self.university,
            total_students=0,
            created_at=date(2000, 1, 1),
        )

        # create the batch
        self.batch = Batch.objects.create(
            department=self.department,
            batch_number=1,
            start_date=date(2001, 1, 1),
            total_students=20,
        )

    def test_mamun(self):
        print(self.batch.end_date)
        print(str(self.department))
