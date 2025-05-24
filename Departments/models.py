from django.db import models
from university.models import University
import logging

logger = logging.getLogger("departments.model")

class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    university = models.ForeignKey(
        University,
        verbose_name="University",
        on_delete=models.CASCADE,
        related_name="departments"
    )



    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.university.name})"

    @property
    def student_count(self):
        count = self.students.count()
        logger.info(f"Accessed student count for department '{self.name}': {count}")
        return count

    def save(self, *args, **kwargs):
        if self.pk:
            old = Department.objects.get(pk=self.pk)
            if old.department_head != self.department_head:
                logger.info(
                    f"Department head for '{self.name}' changed from "
                    f"'{old.department_head}' to '{self.department_head}'"
                )
        else:
            logger.info(f"New department created: {self.name} under {self.university.name}")
        super().save(*args, **kwargs)
