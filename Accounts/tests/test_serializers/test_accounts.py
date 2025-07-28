from Accounts.tests.test_serializers.base import TestBaseSerializer
from Accounts.serializers import AccountSerializer

class TestAccountSerializer(TestBaseSerializer):

    def test_account_serializer_with_valid_user(self):
        serializer = AccountSerializer(data=self.valid_account_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        account = serializer.save()
        
        self.assertEqual(account.user.email, self.valid_user_data["email"])
        self.assertEqual(account.bio, self.valid_account_data["bio"])

    def test_account_serializer_user_validation_fails(self):
        data = self.valid_account_data.copy()
        data["user"]["confirm_password"] = "wrongpass"

        serializer = AccountSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("user", serializer.errors)
        self.assertIn("confirm_password", serializer.errors["user"])

    def test_account_serializer_rejects_missing_user(self):
        data = self.valid_account_data.copy()
        del data["user"]

        serializer = AccountSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("user", serializer.errors)
