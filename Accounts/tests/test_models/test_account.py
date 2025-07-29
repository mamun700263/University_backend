from django.test import TestCase
from Accounts.models import Account
from .account_mixins import AccountTestMixin
from datetime import date

class TestAccount(AccountTestMixin):
    def setUp(self):
        self.user = self.create_user("baseuser@x.com")
        self.account = self.create_account(self.user,"2002-12-12","01712345678")

    def test_account_str(self):
        self.assertEqual(str(self.account), "baseuser@x.com")

    def test_unique_id_autogenerates(self):
        self.assertIsNotNone(self.account.unique_id)
        self.assertTrue(self.account.unique_id.startswith(""))

    def test_mobile_validation(self):
        self.assertEqual(self.account.mobile, "01712345678")
