import time

from django.test import TestCase
from django.utils import timezone

from .models import University
from .serializers import UniversitySerializer

# Create your tests here.


class UniversityModelTest(TestCase):

    def setUp(self):
        self.university = University.objects.create(
            name="Test University",
            starting_date="2024-09-01",
            established_date=timezone.now(),
            updated_at=timezone.now(),
        )

    def test_university_name(self):
        self.assertEqual(self.university.name, "Test University")

    def test_created_at_timestamp(self):
        self.assertIsNotNone(self.university.established_date)

    def test_str_method(self):
        print(str(self.university))


# class University


class UniversitySerializerTestCase(TestCase):
    def setUp(self):
        # create a university instance
        self.university = University.objects.create(
            name="Test University",
            starting_date=timezone.now(),
            established_date="2024-09-01",
            updated_at=timezone.now(),
        )

    def test_serialization(self):
        # Serialize the model instance
        serializer = UniversitySerializer(self.university)
        print("Check before update:")
        print(serializer.data)

        # Update the model instance
        time.sleep(4)
        self.university.name = "Update University"
        self.university.save()  # Save the changes to the database

        # Reinitialize the serializer to reflect changes
        serializer = UniversitySerializer(self.university)
        print("Check after update:")
        print(serializer.data)
