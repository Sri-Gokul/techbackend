from django.urls import path
from .views import *
from django.conf.urls import url 

urlpatterns=[
    path("product/",ProductListView.as_view()),
    path("product/<pk>", ProductDetialView.as_view()),

    path("P/",YuviproductListView.as_view()),
    path("p/<pk>",YuviproductDetialView.as_view())
]