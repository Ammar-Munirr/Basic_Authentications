from hmac import compare_digest

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import (
    validate_password as PasswordValidator,
)
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from api.users.serializers import ShortUserSerializer

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[PasswordValidator],
    )

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "confirm_password",
            "name",
            "image",
        )

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.pop("confirm_password", None)

        if not compare_digest(password, confirm_password):
            raise serializers.ValidationError({"password": "Passwords do not match"})

        return super().validate(attrs)

    def create(self, validated_data):
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.save(update_fields=["password"])
        return user


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        try:
            validate_attrs = super().validate(attrs)
        except Exception as e:
            raise serializers.ValidationError({"password": [str(e)]})

        validate_attrs["user"] = ShortUserSerializer(self.user).data
        return validate_attrs


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            raise serializers.ValidationError({"token": "Invalid token !"})
