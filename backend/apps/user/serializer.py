import os
from uuid import uuid4

# rest frame work imports
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import AuthUserModel as User

# custom made imports
from .validate_password import validate_password

# django main imports


class UserSerializer(serializers.ModelSerializer):
    """
    User updating serializer

    can take all the fields in the user model and update if the
    user is authenticated
    """

    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=False
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "profile_picture",
            "password",
            "is_staff",
            "is_active",
        ]

    def update(self, instance, validated_data):
        """
        It takes in a request and will update the user

        if a user profile image exists these functions make sure to
        delete it in order not to make multiple files that does't necessarily are
        being used
        """
        password = None
        try:
            password = validated_data["password"]
        except Exception as _:
            pass

        try:
            image = validated_data["profile_picture"]
            if instance.profile_picture:
                try:
                    os.remove(instance.profile_picture.path)
                except Exception as _:
                    # file doesn't exist
                    pass
        except Exception:
            # profile picture doesn't exist
            image = None

        if image:
            image.name = rename_file(image)
            instance.profile_picture.delete()

        for key, value in validated_data.items():
            if key == "profile_picture":
                setattr(instance, key, image)
                continue
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance


class RegisterSerializer(serializers.ModelSerializer):
    """
    serializer for creating a new user

    it takes user name, email and password
    check the existence of the user name and email and
    make a new user

    if there is any error returns response of the error

    ### TODO: make the try catch block more efficient
    """

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "profile_picture",
            "password",
            "password2",
            "is_staff",
            "is_active",
        ]

    def validate(self, attrs):
        password = validate_password(attrs["password"])
        messages = {}
        if password:
            for index, error_type in enumerate(password):
                messages[f"password validation error {index}"] = error_type

        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        if messages:
            raise serializers.ValidationError({"password": messages})

        return attrs

    def create(self, validated_data):
        try:
            profile_picture = validated_data["password"]
        except Exception as _:
            profile_picture = None

        if validated_data["is_staff"]:
            user = User.objects.create_staffuser(
                username=validated_data["username"],
                email=validated_data["email"],
                password=validated_data["password"],
                profile_picture=profile_picture,
                is_staff=True,
            )
        else:
            user = User.objects.create_user(
                username=validated_data["username"],
                email=validated_data["email"],
                password=validated_data["password"],
                profile_picture=profile_picture,
                is_staff=False,
            )
        user.save()
        return user


def rename_file(file):
    """
    Takes in a file and clean it from white space and return the file name with
    file name changed to file name + uuid4

    it ensure that there will be no duplicates in the data base
    """
    name, extension = os.path.splitext(file.name)
    name = "".join(name.split())

    return name + "-" + str(uuid4())[:10] + extension

