import logging
from .base import BaseUniversityTest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.utils import timezone
from university.models import University

logger = logging.getLogger("university.test.models")


class UniversityModelTest(BaseUniversityTest):
    """
    Test suite for University model — field validations, constraints, and behaviors.
    """

    # --- BASIC FIELD BEHAVIOR ---

    def test_name_value_is_saved_correctly(self):
        logger.debug("[T01] Verifying university.name is saved correctly...")
        self.assertEqual(self.university.name, "Test University")
        logger.info("✅ [T01] Name field saves value correctly.")

    def test_established_date_value_is_saved(self):
        logger.debug("[T02] Checking if established_date is set...")
        self.assertIsNotNone(self.university.established_date)
        logger.info("✅ [T02] established_date field set correctly.")

    def test_auto_timestamps_are_created(self):
        logger.debug("[T03] Verifying starting_date and updated_at are auto-generated...")
        self.assertIsNotNone(self.university.starting_date)
        self.assertIsNotNone(self.university.updated_at)
        logger.info("✅ [T03] Auto timestamps present.")

    def test_str_dunder_returns_name(self):
        logger.debug("[T04] Checking __str__ method...")
        self.assertEqual(str(self.university), "Test University")
        logger.info("✅ [T04] __str__ returns name.")

    # --- VALIDATION TESTS ---

    def test_name_cannot_be_blank(self):
        logger.debug("[T05] Validating blank name field raises error...")
        self.university.name = ''
        with self.assertRaises(ValidationError):
            self.university.full_clean()
        logger.info("✅ [T05] Blank name rejected.")

    def test_name_must_meet_min_length(self):
        logger.debug("[T06] Testing MinLengthValidator on name...")
        self.university.name = 'Short'
        with self.assertRaises(ValidationError):
            self.university.full_clean()
        logger.info("✅ [T06] MinLengthValidator triggered for short name.")

    def test_established_date_cannot_be_in_future(self):
        logger.debug("[T07] Verifying future established_date triggers error...")
        self.university.established_date = timezone.now().date() + timezone.timedelta(days=1)
        with self.assertRaises(ValidationError):
            self.university.full_clean()
        logger.info("✅ [T07] Future dates rejected as expected.")

    # --- DATABASE CONSTRAINTS ---

    def test_name_must_be_unique(self):
        logger.debug("[T08] Verifying unique constraint on name field...")
        with self.assertRaises(IntegrityError):
            University.objects.create(
                name="Test University",
                established_date="2020-01-01"
            )
        logger.info("✅ [T08] Unique name constraint enforced.")
