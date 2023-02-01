from django.contrib import admin
from burgerAPI.models import UserProfile, Ingredient, CustomerDetail, Order

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Ingredient)
admin.site.register(CustomerDetail)
admin.site.register(Order)