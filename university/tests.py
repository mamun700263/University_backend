from django.test import TestCase
from .models import University

from django.utils import timezone
# Create your tests here.

class UniversityModelTest(TestCase):
    
    def setUp(self):
        self.university = University.objects.create(
            name="Test University",
            starting_date = "2024-09-01",
            established_date = timezone.now(),
            updated_at = timezone.now()
        )
    def test_university_name(self):
        self.assertEqual(self.university.name,"Test University")
    
    def test_created_at_timestamp(self):
        self.assertIsNotNone(self.university.established_date)
    def test_str_method(self):
        print(str(self.university))
        

from rest_framework.test import APITestCase
from .models import University
from .Serializer import UniversitySerializer

class UniversitySerializerTestCase(APITestCase):
    def setUp(self):
        # Create a sample University object
        self.university = University.objects.create(
            name="Test University",
            established_date="2000-01-01",
        )
        self.serializer_data = {
            'name': "Another University",
            'established_date': "2010-01-01",
        }

    def test_serialization(self):
        # Serialize the University object
        serializer = UniversitySerializer(self.university)
        data = serializer.data

        # Check if the serialized data matches the instance data
        self.assertEqual(data['name'], self.university.name)
        # self.assertEqual(data['location'], self.university.location)
        self.assertEqual(data['established_date'], self.university.established_date)
        # self.assertEqual(data['total_students'], self.university.total_students)

    def test_deserialization_with_valid_data(self):
        # Deserialize valid data
        serializer = UniversitySerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        university = serializer.save()

        # Check if the new object is saved correctly
        self.assertEqual(university.name, self.serializer_data['name'])
        # self.assertEqual(university.location, self.serializer_data['location'])
        self.assertEqual(str(university.established_date), self.serializer_data['established_date'])
        # self.assertEqual(university.total_students, self.serializer_data['total_students'])

    def test_deserialization_with_invalid_data(self):
        # Test with missing fields
        invalid_data = {'name': "Invalid University"}
        serializer = UniversitySerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        # self.assertIn('location', serializer.errors)
        self.assertIn('established_date', serializer.errors)
        # self.assertIn('total_students', serializer.errors)
