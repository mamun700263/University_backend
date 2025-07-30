
from rest_framework import serializers


from Accounts.models import StudentAccount
from rest_framework import serializers

from .models import Department



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

