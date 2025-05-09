from django.db import models


class University(models.Model):
    """
    Represents a university with its departments and leadership.
    """

    name = models.CharField(max_length=100, unique=True)
    starting_date = models.DateTimeField(auto_now_add=True)
    established_date = models.DateField(
        blank=False,
        null=False
    )  # Automatically adds timestamp
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"
        ordering = ["name"]

    def __str__(self):
        return self.name  # Displays the university name as a string
