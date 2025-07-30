from Departments.models import Department
from datetime import date
from university.tests.base import BaseUniversityTest
class BaseDepartmentTest(BaseUniversityTest):

    def setUp(self):
        super().setUp()
        self.department = Department.objects.create(
            name='Test Department',
            short_name='TD',
            created_at=date(2025, 1, 1),
            university=self.university,
        )