from django.test import TestCase
from university.models import University
from datetime import date
import logging

from django.utils import timezone
logger = logging.getLogger('university.test.base')

class BaseUniversityTest(TestCase):
    """
    Base test case providing a shared University instance setup
    for all University-related test classes.
    """

    def setUp(self):
        self.university = University.objects.create(
            name="Test University",
            starting_date=date(2024, 9, 1),
            established_date=timezone.now().date(),
            updated_at=timezone.now(),
        )
        logger.info("🧪 [%s] University test instance created: %s", self.__class__.__name__, self.university.name)
