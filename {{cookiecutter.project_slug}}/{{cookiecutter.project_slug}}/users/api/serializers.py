from django.contrib.auth import get_user_model
from rest_framework import serializers

from {{ cookiecutter.project_slug }}.users.models import User as UserType


User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    class Meta:
        model = User
        {%- if cookiecutter.username_type == "email" %}
        fields = ["name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }
        {%- else %}
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        }
        {%- endif %}


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
        )

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
