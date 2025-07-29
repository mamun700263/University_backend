from django.db import models
from django.utils import timezone


class Enrollment(models.Model):
    student = models.ForeignKey("Accounts.StudentAccount", on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="enrollments")
    enrolled_at = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=2, null=True, blank=True)
    semester = models.CharField(max_length=20)

    class Meta:
        unique_together = ("student", "course", "semester")
        ordering = ["-enrolled_at"]

    def __str__(self):
        return f"{self.student} -> {self.course} ({self.semester})"
