from django.shortcuts import render
from .serializers import ProductSerializer , YuviproductSerializer
from tech.models import Product ,Yuviproduct
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework import permissions, authentication


class ProductListView(generics.ListAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer

     permission_classes=[permissions.AllowAny,]
     authentication_classes=[authentication.TokenAuthentication]

class ProductDetialView(generics.RetrieveAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer

     permission_classes=[permissions.AllowAny,]
     authentication_classes=[authentication.TokenAuthentication]

class YuviproductListView(generics.ListAPIView):
     queryset = Yuviproduct.objects.all()
     serializer_class = YuviproductSerializer

     permission_classes=[permissions.AllowAny,]
     authentication_classes=[authentication.TokenAuthentication]

class YuviproductDetialView(generics.RetrieveAPIView):
     queryset = Yuviproduct.objects.all()
     serializer_class = YuviproductSerializer

     permission_classes=[permissions.AllowAny,]
     authentication_classes=[authentication.TokenAuthentication]