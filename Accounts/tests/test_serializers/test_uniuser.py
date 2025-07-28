from Accounts.serializers import UserSerializer
from Accounts.models import UniUser
from Accounts.tests.test_serializers import TestBaseSerializer


class UniUserSerializerTest(TestBaseSerializer):

    def test_valid_user_serializer(self):
        serializer = UserSerializer(data=self.valid_user_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        user = serializer.save()

        self.assertEqual(user.email, self.valid_user_data["email"])
        self.assertEqual(user.full_name, "Test User")
        self.assertTrue(user.check_password("securepass123"))
        self.assertTrue(user.is_active)
        self.assertEqual(user.role, UniUser.Roles.STUDENT) 

    def test_password_mismatch_fails(self):
        data = self.valid_user_data.copy()
        data["confirm_password"] = "wrongpass"

        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("confirm_password", serializer.errors)

    def test_missing_required_fields(self):
        serializer = UserSerializer(data={})
        self.assertFalse(serializer.is_valid())
        required_fields = ["email","password", "confirm_password"]
        for field in required_fields:
            self.assertIn(field, serializer.errors)
