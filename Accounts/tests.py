from django.test import TestCase
from .models import Account, User

class TestAccount(TestCase):
    def setUp(self):
        user = User.objects.create(
            username:'test user1',
            password:'Helloworld1'
        )
        account = Account.objects.create(
            ''
        )