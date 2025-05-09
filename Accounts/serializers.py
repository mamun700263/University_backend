from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Account,
    AuthorityAccount,
    StaffAccount,
    StudentAccount,
    TeacherAccount
    )


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "confirm_password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        # Remove confirm_password after validation
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.is_active = False  # Default inactive status
        user.save()
        return user


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = [
            "id",
            "user",
            "date_of_birth",
            "unique_id",
            "bio",
            "mobile",
            "profile_picture",
        ]
        read_only_fields = ["unique_id"]

    def create(self, validated_data):
        # Extract user data
        user_data = validated_data.pop("user")

        # Use UserSerializer to validate and create the user
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()

        # Add the created user to validated_data
        validated_data["user"] = user

        # Create and return the Account object
        return super().create(validated_data)


class StudentAccountSerializer(AccountSerializer):
    class Meta(AccountSerializer.Meta):
        model = StudentAccount
        fields = AccountSerializer.Meta.fields + [
            "Class_Representetive",
            "batch",
        ]


class TeacherAccountSerializer(AccountSerializer):
    class Meta(AccountSerializer.Meta):
        model = TeacherAccount
        fields = AccountSerializer.Meta.fields + [
            "Department_head",
        ]


class StaffAccountSerializer(AccountSerializer):
    class Meta(AccountSerializer.Meta):
        model = StaffAccount
        fields = AccountSerializer.Meta.fields


class AuthorityAccountSerializer(AccountSerializer):
    class Meta(AccountSerializer.Meta):
        model = AuthorityAccount
        fields = AccountSerializer.Meta.fields


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
