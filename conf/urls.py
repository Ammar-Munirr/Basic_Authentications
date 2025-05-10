from django.contrib import admin
from django.urls import include, path

from api.users.views import redirect_api


urlpatterns = [
    path("", redirect_api,name='redirect'),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
