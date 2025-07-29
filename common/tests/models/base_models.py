
from datetime import date

from django.test import TestCase
from django.utils import timezone

from batch.models import Batch
from Departments.models import Department
from university.models import University
from Accounts.models import Account

from django.contrib.auth import get_user_model


User = get_user_model()

class UniversityTestBase(TestCase):
    """
    Central test base that sets up a University, Department, and Batch.
    Provides helper methods to create users and other entities.
    """

    def setUp(self):
        self.university = self.create_university()
        self.department = self.create_department(self.university)
        self.batch = self.create_batch(self.department)

    # === Setup helpers ===
    def create_university(self, name="Test University", established_date=date(2000, 1, 2)):
        return University.objects.create(
            name=name,
            established_date=established_date,
            starting_date=timezone.now().date(),
            updated_at=timezone.now()
        )

    def create_department(self, university=None, name="Computer Science", short_name="CSE"):
        if university is None:
            university = self.create_university()
        return Department.objects.create(
            name=name,
            short_name=short_name,
            created_at=timezone.now().date(),
            university=university
        )

    def create_batch(self, department, batch_number=1, total_students=0):
        return Batch.objects.create(
            department=department,
            batch_number=batch_number,
            total_students=total_students,
            start_date=timezone.now().date()
        )

    def create_user(self,
        email="testuser@test.com",
        password="strongpass123",
        full_name="User"
        ):

        return User.objects.create_user(
            email=email,
            password=password,
            full_name=full_name
        )

    def create_account(self, 
        user=None, 
        date_of_birth="2002-12-12", 
        mobile="0123481230948"
        ):

        if user is None:
            user = self.create_user()
        return Account.objects.create(
            user=user,
            date_of_birth=date_of_birth,
            mobile=mobile,
        )



