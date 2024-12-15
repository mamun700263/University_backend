from django.test import TestCase
from .models import University

from django.utils import timezone
# Create your tests here.

class UniversityModelTest(TestCase):
    
    def setUp(self):
        self.university = University.objects.create(
            name="Test University",
            starting_date = "2024-09-01",
            created_at = timezone.now(),
            updated_at = timezone.now()
        )
    def test_university_name(self):
        self.assertEqual(self.university.name,"Test University")
    
    def test_created_at_timestamp(self):
        self.assertIsNotNone(self.university.created_at)
    def test_str_method(self):
        print(str(self.university))