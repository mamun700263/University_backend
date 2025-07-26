from django.test import TestCase
from Accounts.models import StaffAccount
from .account_mixins import AccountTestMixin
from datetime import date

class TestAuthorityAccount(TestCase, AccountTestMixin):
    def setUp(self):
        self.user = self.create_user("staff@x.com")
        self.authority = StaffAccount.objects.create(
            user=self.user,
            date_of_birth=date(1990, 2, 2)
        )

    def test_authority_unique_id(self):
        self.assertTrue(self.authority.unique_id.startswith("OF-"))
