from django.test import TestCase
from Accounts.models import StudentAccount
from .account_mixins import AccountTestMixin
from datetime import date

class TestStudentAccount(TestCase, AccountTestMixin):
    def setUp(self):
        self.user = self.create_user(email="student1@x.com")
        self.university = self.create_university(name='mamun University')
        self.department = self.create_department(university=self.university)
        self.batch = self.create_batch(self.department, total_students=5)
        self.student = StudentAccount.objects.create(
            user=self.user,
            date_of_birth=date(2000, 1, 1),
            batch=self.batch,
            Class_Representetive=True
        )

    def test_student_unique_id(self):
        self.assertEqual(self.student.unique_id,'STCSE001006')
        self.assertIn("CSE", self.student.unique_id)

    def test_batch_student_count_increments(self):
        self.assertEqual(self.batch.total_students, 6)

    