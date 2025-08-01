# accounts/tests/test_authority_account.py

from django.test import TestCase
from Accounts.models import AuthorityAccount
from .account_mixins import AccountTestMixin
from datetime import date

class TestAuthorityAccount(TestCase, AccountTestMixin):
    def setUp(self):
        self.user = self.create_user("authority1")
        self.authority = AuthorityAccount.objects.create(
            user=self.user,
            date_of_birth=date(1990, 2, 2)
        )

    def test_authority_unique_id(self):
        self.assertTrue(self.authority.unique_id.startswith("AU-"))
