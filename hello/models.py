from ctypes import addressof
from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import NullBooleanField

# Create your models here.

class plant(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.TextField(max_length=50)
    city = models.TextField(max_length=60)
    type_of_plant = models.TextField(max_length=30)
    price = models.IntegerField()
    soil_type =  models.TextField(max_length=50)
    def __str__(self):
        return self.product_name
class farmer(models.Model):
    farmer_id = models.IntegerField(primary_key=True)
    contact_no = models.BigIntegerField()
    farmer_name = models.TextField(max_length=40)
    place = models.TextField(max_length=40)
   
    def __str__(self):
        return self.farmer_name
    

class seeds(models.Model):
    seed_name = models.TextField(max_length=100)
    seed_id = models.IntegerField(primary_key=True)
    price = models.IntegerField()
    soil_type = models.TextField(max_length=100)
    
    def __str__(self):
        return self.seed_name



    def __str__(self):
        return self.customer_name


class meta:
        unique_together=(('customer_id','product_id'),)
  
class seed_purchased(models.Model):
    farmer_id = models.ForeignKey(farmer,on_delete=models.CASCADE)
    seed_id = models.ForeignKey(seeds,on_delete=CASCADE)

    class meta:
        unique_together=(('farmer_id','seed_id'),)
  

class plant_purchased(models.Model):

    farmer_id = models.ForeignKey(farmer,on_delete=models.CASCADE)
    product_id = models.ForeignKey(plant,on_delete=CASCADE)
   

    class meta:
        unique_together=(('farmer_id','product_id'),)

class Hello(models.Model):
    email_id = models.EmailField(max_length=100,blank=True)
    customer_name = models.TextField(max_length=30)
    phone_no = models.BigIntegerField()
    customer_id = models.IntegerField(primary_key=True)
    Order=models.ManyToManyField(plant)
    def __str__(self):
        return self.customer_name

class Customer(models.Model):
    username=models.TextField()
    mobilenumber=models.BigIntegerField()
    emailid=models.EmailField()
    pwd=models.CharField(max_length=100)
    address=models.TextField()
    pincode=models.IntegerField()

class Products(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.TextField()
    product_botname=models.TextField(null=True)
    product_type=models.CharField(max_length=100)
    product_price=models.IntegerField()
    soil_type=models.TextField()
    orders=models.ManyToManyField(Customer)
    product_image=models.ImageField(upload_to="hello/static/images")
    def __str__(self):
        return self.product_name

class Order(models.Model):
 customername=models.TextField(null=True)
 product_id=models.IntegerField()
 productname=models.TextField()
 Date=models.DateField(null=True)
