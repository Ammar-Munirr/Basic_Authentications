from django.urls import path
from rest_framework.routers import DefaultRouter

from api.jwtauth.views import LoginViewset, LogoutView

router = DefaultRouter(trailing_slash=False)


urlpatterns = [
    path("login", LoginViewset.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
] + router.urls
