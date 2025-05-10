from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.core.swagger.swagger_conf import schema_view
from api.jwtauth.views import RegistrationViewSet
from api.users.views import ProfileViewset

router = DefaultRouter(trailing_slash=False)
router.register(r"register", RegistrationViewSet, basename="register")
router.register(r"profile", ProfileViewset, basename="profile")


urlpatterns = [
    path("auth/", include("api.jwtauth.urls")),
    path("documentation/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
] + router.urls
