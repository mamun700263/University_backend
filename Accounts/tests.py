from django.test import TestCase
from django.utils import timezone

from .models import (Department, Student, TeacherAccount, University)


class DepartmentsModelTest(TestCase):
    """Test case for Department model"""

    def setUp(self):
        """
        Set up test data for the Department model.
        """
        # Create a university instance
        self.university = University.objects.create(
            name="Sample University",
            starting_date=timezone.now().date()
        )

        # Create a TeacherAccount instance (assuming TeacherAccount exists)
        self.teacher = TeacherAccount.objects.create(
            username="teacher1",
            password="password",
            email="teacher1@example.com"
        )

        # Create a Department instance
        self.department = Department.objects.create(
            name="Computer Science",
            university=self.university,
            department_head=self.teacher,
            total_students=100,
            created_at=timezone.now().date(),
        )

    def test_department_creation(self):
        """Test that a department is created correctly."""
        department = self.department
        self.assertEqual(department.name, "Computer Science")
        self.assertEqual(department.university.name, "Sample University")
        self.assertEqual(department.department_head.username, "teacher1")
        self.assertEqual(department.total_students, 100)

    def test_department_str(self):
        """Test the string representation of the Department."""
        self.assertEqual(
            str(self.department),
            "Computer Science (Sample University)"
            )

    def test_student_count_property(self):
        """Test the student_count property."""
        # Assuming the `Student` model has a foreign key to `Department`
        # Create some Student instances for this department
        Student.objects.create(department=self.department, name="Student 1")
        Student.objects.create(department=self.department, name="Student 2")

        # Now check the student count
        self.assertEqual(self.department.student_count, 2)

    def test_department_head_null(self):
        """Test if department head can be null."""
        department_without_head = Department.objects.create(
            name="Mathematics",
            university=self.university,
            department_head=None,
            total_students=50,
            created_at=timezone.now().date(),
        )
        self.assertIsNone(department_without_head.department_head)

    def test_department_update(self):
        """Test updating a department."""
        # Update department details
        self.department.name = "Electrical Engineering"
        self.department.total_students = 200
        self.department.save()
        updated_department = Department.objects.get(id=self.department.id)
        self.assertEqual(
            updated_department.name,
            "Electrical Engineering"
            )
        self.assertEqual(
            updated_department.total_students,
            200
            )
