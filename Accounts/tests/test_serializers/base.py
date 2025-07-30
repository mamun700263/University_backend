from rest_framework.test import APITestCase


class TestBaseSerializer(APITestCase):
    def setUp(self):
        self.valid_user_data = {
            "email": "user@example.com",
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "password": "securepass123",
            "confirm_password": "securepass123",
        }

        self.valid_account_data ={
            "user":self.valid_user_data,
            "mobile": "01712345678",
            "bio": "Elite bio",
            "date_of_birth": "2000-01-01",
        }
