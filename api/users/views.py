from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.users.serializers import ShortUserSerializer


class ProfileViewset(GenericViewSet):
    serializer_class = ShortUserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, url_path="me", methods=["GET"])
    def me(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response({"data": [serializer.data]}, status=status.HTTP_200_OK)


def redirect_api(request):
    return redirect("schema-swagger-ui")
