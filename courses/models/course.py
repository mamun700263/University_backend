from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Course(models.Model):
    title = models.CharField(
        max_length=120,
        unique=True,
    )
    taken_by = models.ForeignKey(
        "Accounts.TeacherAccount",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses"
    )
    credit = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(0.5),
            MaxValueValidator(4.0)
        ],
        help_text="Credit must be between 0.5 and 4.0"
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"{self.title} ({self.credit} Credits)"



