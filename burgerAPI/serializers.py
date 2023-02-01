from rest_framework.serializers import ModelSerializer

from burgerAPI.models import CustomerDetail, Ingredient, Order, UserProfile


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

class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        exclude = [
            "id",
        ]

class CustomerDetailSerializer(ModelSerializer):
    class Meta:
        model = CustomerDetail
        exclude = [
            "id",
        ]

class OrderSerializer(ModelSerializer):
    ingredients = IngredientSerializer()
    customer = CustomerDetailSerializer()

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        ingredient_data = validated_data.pop("ingredients") # same as valiedated_data['ingredients']
        ingredients = IngredientSerializer.create(
            IngredientSerializer(), validated_data=ingredient_data
        )
        
        customer_data = validated_data.pop("customer")
        customer = CustomerDetailSerializer.create(
            CustomerDetailSerializer(), validated_data=customer_data
        )
        
        order, created = Order.objects.update_or_create(
            ingredients=ingredients,
            customer=customer,
            price=validated_data.pop("price"),
            orderTime=validated_data.pop("orderTime"),
            user=validated_data.pop("user"),
        )

        return order