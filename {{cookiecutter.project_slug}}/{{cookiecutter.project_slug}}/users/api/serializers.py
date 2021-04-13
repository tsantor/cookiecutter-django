from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


# -----------------------------------------------------------------------------
# My forked version
# -----------------------------------------------------------------------------


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            # "username",
            "first_name",
            "last_name",
            "name",
            "email",
            "password",
        )

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        "token": token,
        "user": MyUserSerializer(user, context={"request": request}).data,
    }
