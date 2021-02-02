from rest_framework import serializers
from tech.models import Product , Yuviproduct
from drf_extra_fields.fields import Base64ImageField

class ProductSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
         model = Product
         fields = "__all__"

class YuviproductSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
         model = Yuviproduct
         fields = "__all__"