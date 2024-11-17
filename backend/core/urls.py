from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("user.urls")),
    path("blog/", include("blog.urls")),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
]
