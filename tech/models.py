from django.db import models
from drf_extra_fields.fields import Base64ImageField

# Create your models here.
class Product(models.Model):
    
    name= models.CharField(max_length=120)
    image = models.ImageField(blank=False, null=False)
    description=models.CharField(max_length=120)
    oldcost=models.CharField(max_length=120)
    newcost=models.CharField(max_length=120)
    discount=models.CharField(max_length=120)
 
    def __str__(self):
        return self.name

class Yuviproduct(models.Model):
    
    name= models.CharField(max_length=120)
    image = models.ImageField(blank=False, null=False)
    description=models.CharField(max_length=120)
    oldcost=models.CharField(max_length=120)
    newcost=models.CharField(max_length=120)
    like=models.CharField(max_length=120)
 
    def __str__(self):
        return self.name