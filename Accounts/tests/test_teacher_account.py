
from django.test import TestCase
from Accounts.models import TeacherAccount
from .mixins import AccountTestMixin
from datetime import date

class TestTeacherAccount(TestCase, AccountTestMixin):
    def setUp(self):
        self.user = self.create_user("teacher1")
        self.university = self.create_university()
        self.department = self.create_department(self.university,"Electricla Engineerign",'EEE')
        self.teacher = TeacherAccount.objects.create(
            user=self.user,
            date_of_birth=date(1985, 5, 5),
            department=self.department,
            Department_head=True
        )

    def test_teacher_unique_id(self):
        self.assertTrue(self.teacher.unique_id.startswith("TE"))
    
    def test_department(self):
        self.assertEqual('EEE',self.department.short_name)
