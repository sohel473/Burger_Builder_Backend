
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from burgerAPI.models import Order, UserProfile
from burgerAPI.serializers import OrderSerializer, UserProfileSerializer

# Create your views here.
class UserProfileViewSet(ModelViewSet):
  queryset = UserProfile.objects.all()
  serializer_class = UserProfileSerializer
    

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
      queryset = Order.objects.all()
      user_id = self.request.query_params.get("user_id", None)
      if id is not None:
          queryset = queryset.filter(user__id=user_id)
      return queryset