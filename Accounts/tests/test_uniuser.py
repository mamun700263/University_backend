from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UniUserModelTests(TestCase):

    def test_user_creation(self):
        user = User.objects.create_user(
            email="user@example.com",
            password="pass1234",
            full_name="Regular User"
        )
        self.assertEqual(user.email, "user@example.com")
        self.assertTrue(user.check_password("pass1234"))
        self.assertEqual(user.role, User.Roles.STUDENT)
        self.assertFalse(user.is_superuser)

    def test_superuser_creation(self):
        superuser = User.objects.create_superuser(
            email="admin@example.com",
            password="adminpass",
            full_name="Admin User"
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertEqual(superuser.role, User.Roles.ADMIN)

    def test_role_properties(self):
        teacher = User.objects.create_user(
            email="teacher@example.com",
            password="teachpass",
            full_name="Teacher Guy",
            role=User.Roles.TEACHER
        )
        self.assertTrue(teacher.is_teacher)
        self.assertFalse(teacher.is_student)
        self.assertTrue(teacher.has_role("teacher"))
        self.assertTrue(teacher.has_role("student", "teacher"))
        self.assertFalse(teacher.has_role("admin"))
