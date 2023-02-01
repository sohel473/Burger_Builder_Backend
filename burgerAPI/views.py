
from rest_framework.viewsets import ModelViewSet

from burgerAPI.models import UserProfile
from burgerAPI.serializers import UserProfileSerializer

# Create your views here.
class UserProfileViewSet(ModelViewSet):
  queryset = UserProfile.objects.all()
  serializer_class = UserProfileSerializer
    