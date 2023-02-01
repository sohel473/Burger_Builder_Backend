from rest_framework.serializers import ModelSerializer

from burgerAPI.models import UserProfile


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "email",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        user = UserProfile(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user