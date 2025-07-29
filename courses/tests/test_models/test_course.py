from django.core.exceptions import ValidationError
from django.db import IntegrityError

from Accounts.models import TeacherAccount
from common.tests.models import UniversityTestBase
from courses.models import Course


class CourseModelTest(UniversityTestBase):
    
    def setUp(self):
        self.department = self.create_department()
        self.teacher = TeacherAccount.objects.create(
            user=self.create_user("teacher@test.com"),
            department=self.department,
        )

    def test_course_creation_success(self):
        course = Course.objects.create(
            title="Mathematics",
            taken_by=self.teacher,
            credit=3,
        )
        self.assertEqual(course.title, "Mathematics")
        self.assertEqual(course.credit, 3)
        self.assertEqual(course.taken_by.user.email, "teacher@test.com")

    def test_course_str_representation(self):
        course = Course.objects.create(
            title="Physics",
            taken_by=self.teacher,
            credit=4,
        )
        self.assertEqual(str(course), "Physics (4 Credits)")

    def test_invalid_credit_raises_validation_error(self):
        course = Course(
            title="Chemistry",
            taken_by=self.teacher,
            credit=99999,
        )
        with self.assertRaises(ValidationError):
            course.full_clean()

    def test_course_without_teacher_fails(self):
        with self.assertRaises(IntegrityError):
            Course.objects.create(
                title="Biology",
                taken_by=None,
                credit=3,
            )

    def test_blank_title_fails_validation(self):
        course = Course(
            title="",
            taken_by=self.teacher,
            credit=3,
        )
        with self.assertRaises(ValidationError):
            course.full_clean()

    def test_negative_credit_fails(self):
        course = Course(
            title="History",
            taken_by=self.teacher,
            credit=-1,
        )
        with self.assertRaises(ValidationError):
            course.full_clean()
