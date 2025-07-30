import logging
from rest_framework import serializers
logger = logging.getLogger("account.serializer")

from .models import (
    UniUser,
    Account,
    AuthorityAccount,
    StaffAccount,
    StudentAccount,
    TeacherAccount
    )



class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UniUser
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
            logger.error(f'password miss match {data["password"]} != {data["confirm_password"]}')
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        full_name = f"{validated_data.get('first_name','')} {validated_data.get('last_name','')}".strip()
        
        user = UniUser.objects.create(
            email=validated_data["email"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            full_name=full_name,
            role=validated_data.get("role", UniUser.Roles.STUDENT),
        )
        
        user.set_password(validated_data["password"])
        user.is_active = True
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
        ]
        read_only_fields = ["unique_id"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_serializer = UserSerializer(data=user_data)

        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()

        validated_data["user"] = user
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
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
