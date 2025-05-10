from django.contrib.auth import get_user_model
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenViewBase

from api.jwtauth.serializers import (
    LoginSerializer,
    LogoutSerializer,
    UserCreateSerializer,
)
from api.users.serializers import ShortUserSerializer

User = get_user_model()


class RegistrationViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        refresh = RefreshToken.for_user(user)
        token = dict(refresh=str(refresh), access=str(refresh.access_token))
        token["user"] = ShortUserSerializer(user, context=self.get_serializer_context()).data
        return Response(token, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.validated_data["role"] = User.Roles.USER
        return serializer.save()


class LoginViewset(TokenViewBase):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=LogoutSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: openapi.Response(description="Logout successful"),
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Invalid data"),
            status.HTTP_401_UNAUTHORIZED: openapi.Response(description="Unauthorized user"),
        },
    )
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
