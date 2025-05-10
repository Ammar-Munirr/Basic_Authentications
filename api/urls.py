from django.urls import path

from api.core.swagger.swagger_conf import schema_view

urlpatterns = [
    path("documentation/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
