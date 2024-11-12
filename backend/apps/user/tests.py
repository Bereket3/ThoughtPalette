import os
from pathlib import Path

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from rest_framework.test import APIClient

from .serializer import RegisterSerializer, UserSerializer

User = get_user_model()


class UserSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass123",
            profile_picture=None,
            is_staff=False,
            is_active=True,
        )
        self.client = APIClient()
        self.basedir = Path(__file__).resolve().parent.parent.parent

    def test_update_user_serializer(self):
        """Test updating a user with UserSerializer."""
        data = {
            "username": "newtestuser",
            "email": "newtestuser@example.com",
            "is_active": False,
            "password": "newpassword123",
        }
        serializer = UserSerializer(instance=self.user, data=data, partial=True)

        self.assertTrue(serializer.is_valid())
        serializer.save()

        self.user.refresh_from_db()

        # Assert the changes
        self.assertEqual(self.user.username, data["username"])
        self.assertEqual(self.user.email, data["email"])
        self.assertFalse(self.user.is_active)
        self.assertTrue(self.user.check_password(data["password"]))

    def test_register_user_serializer(self):
        """Test creating a new user with RegisterSerializer."""
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newuserpass123",
            "password2": "newuserpass123",
            "is_staff": False,
        }
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()

        # Assert the created user details
        self.assertEqual(user.username, data["username"])
        self.assertEqual(user.email, data["email"])
        self.assertFalse(user.is_staff)
        self.assertTrue(user.check_password(data["password"]))

    def test_password_mismatch(self):
        """Test password mismatch validation in RegisterSerializer."""
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newuserpass123",
            "password2": "differentpass",
            "is_staff": False,
        }
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
        self.assertEqual(
            serializer.errors["password"][0], "Password fields didn't match."
        )

    def test_profile_picture_update(self):
        """Test updating profile picture in UserSerializer."""
        test_image = os.path.join(self.basedir, "helpers/blank.png")
        with open(test_image, "rb") as f:
            uploaded_file = SimpleUploadedFile(
                name="test_image.jpg", content=f.read(), content_type="image/jpeg"
            )

        data = {"profile_picture": uploaded_file}
        serializer = UserSerializer(instance=self.user, data=data, partial=True)
        self.assertTrue(serializer.is_valid())

        serializer.save()
        self.user.refresh_from_db()

        # Ensure profile picture is updated
        self.assertTrue(self.user.profile_picture.name.startswith("profile_pictures"))
