from django.db import models
from django.utils import timezone
import logging
from django.core.validators import MinLengthValidator
from common.validators.user_validators import validate_not_future_date

from django.core.exceptions import ValidationError

# import logging
logger = logging.getLogger("university.models")





class University(models.Model):
    """
    Represents a university with its departments and leadership.
    """

    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(10)],
        unique=True
        #must contain "university"
    )
    established_date = models.DateField(
        blank=False,
        null=False,
        validators=[validate_not_future_date],
    )
    
    
    starting_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"
        ordering = ["name"]

    def __str__(self):
        return self.name  # Keep __str__ clean — don't log here

    def save(self, *args, **kwargs):
            
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new:
            logger.info("🎓 University created: %s", self.name)
        else:
            logger.info("🛠️ University updated: %s", self.name)
