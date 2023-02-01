
from rest_framework.viewsets import ModelViewSet

from burgerAPI.models import Order, UserProfile
from burgerAPI.serializers import OrderSerializer, UserProfileSerializer

# Create your views here.
class UserProfileViewSet(ModelViewSet):
  queryset = UserProfile.objects.all()
  serializer_class = UserProfileSerializer
    

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()