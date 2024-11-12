from django.contrib.auth.backends import BaseBackend
from .models import AuthUserModel as MyUser


class EmailAuthenticationBackend(BaseBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username'].lower()
        password = kwargs['password']
        try:
            my_user = MyUser.objects.get(email=email)
        except MyUser.DoesNotExist:
            return None
        else:
            if my_user.is_active and my_user.check_password(password):
                return my_user
        return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None