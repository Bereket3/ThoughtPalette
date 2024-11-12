from typing import Any

from django.core.management.base import BaseCommand
from user.models import AuthUserModel as User


class Command(BaseCommand):
    help = "Allow you to create a super user called root"

    def handle(self, *args: Any, **options: Any):
        user_name = User.objects.filter(username="root")
        email = User.objects.filter(email="root@root.com")
        if user_name.exists() or email.exists():
            self.stdout.write(self.style.ERROR("The user already exist jachaa"))
        else:
            self.stdout.write(self.style.WARNING("Createing a use..."))
            root = User.objects.create_superuser(
                username="root", email="root@root.com", password="root"
            )
            root.save()
            self.stdout.write(
                self.style.SUCCESS(
                    "The user was created successfully now u can log with root"
                )
            )

