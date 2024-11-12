from django.urls import path


from .views import (
    CreateUserAPIView,
    ListUserAPIView,
    UpdateAndGetUserAPIView,

    ListTestimonyAPIView,
    CreatTestimonyAPIView,
    GetUpdateAndDeleteTestimonyAPIView,
)

urlpatterns = [
    # testimony api's
    path('testimony/create/', CreatTestimonyAPIView.as_view(), name='create-testimony'),
    path('testimony/<str:id>/', GetUpdateAndDeleteTestimonyAPIView.as_view(), name='update-delete-testimony'), 
    path('testimony/', ListTestimonyAPIView.as_view(), name='list-testimony'),
    # user api
    path('create/', CreateUserAPIView.as_view(), name='create-user'),
    path('<str:id>/', UpdateAndGetUserAPIView.as_view(), name='update-user'),
    path('', ListUserAPIView.as_view(), name='list-user'),  
]