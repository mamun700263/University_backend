from django.contrib.auth.models import User
from datetime import date
from Departments.models import Department
from batch.models import Batch
from university.models import University

class AccountTestMixin:

    def create_user(
            self,
            username="testuser@test.com",
            password="strongpass123"
            ):
        return User.objects.create_user(
            username=username,
            password=password
            )
    
    def create_university(self,
        name='Test University',
        established_date = date(2000,1,2)
        ):
        return University.objects.create(
            name = name,
            established_date= established_date
        )
    
    def create_department(self,
        university,
        department_name = 'Computer Science',
        short_name="CSE"
        ):
        return Department.objects.create(
            short_name=short_name,
            name = department_name,
            university = university
        )

    def create_batch(self,department, total_students=0):
        return Batch.objects.create(
            department = department,
            total_students=total_students,
            batch_number=1,
            start_date = date(2025,1,1)
        )
