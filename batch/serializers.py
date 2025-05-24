from rest_framework import serializers

from Accounts.models import StudentAccount
from .models import Batch




class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"

    def student_count(self):
        students = StudentAccount.objects.get( batch=self.model).count()
