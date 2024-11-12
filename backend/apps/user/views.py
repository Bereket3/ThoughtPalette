from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from .models import AuthUserModel
from .serializer import RegisterSerializer, UserSerializer


class CreateUserAPIView(CreateAPIView):
    queryset = AuthUserModel
    serializer_class = RegisterSerializer


class UpdateAndGetUserAPIView(UpdateAPIView, RetrieveAPIView):
    queryset = AuthUserModel
    serializer_class = UserSerializer
    lookup_field = "id"


class ListUserAPIView(ListAPIView):
    queryset = AuthUserModel.objects.all()
    serializer_class = UserSerializer

