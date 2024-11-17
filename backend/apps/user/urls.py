from django.urls import path

from .views import CreateUserAPIView, ListUserAPIView, UpdateAndGetUserAPIView

urlpatterns = [
    # user api
    path("create/", CreateUserAPIView.as_view(), name="create-user"),
    path("<str:id>/", UpdateAndGetUserAPIView.as_view(), name="update-user"),
    path("", ListUserAPIView.as_view(), name="list-user"),
]

