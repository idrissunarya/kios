from django.db import models
import uuid


class Material(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product_upload', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    password =models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.username

class Storage(models.Model):
    KG = 'KG'
    ML = 'ML'
    BOX = 'BOX'
    PCS = 'PCS'
    L = 'L'
    UNIT_IN_CHOICES = (
        (KG, 'Kilogram'),
        (ML, 'Mililitre'),
        (BOX, 'Box'),
        (PCS, 'Pcs'),
        (L, 'Litre'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.ForeignKey('Material', on_delete=models.CASCADE)
    unit = models.CharField(max_length=3,choices=UNIT_IN_CHOICES,default=KG,)
    qty = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.unit

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=256)
    city_ascii = models.CharField(max_length=256)
    lat = models.CharField(max_length=256)
    lng	= models.CharField(max_length=256)
    country	= models.CharField(max_length=256)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    admin_name = models.CharField(max_length=256)
    capital	= models.CharField(max_length=64)
    population = models.CharField(max_length=256)

    def __str__(self):
        return self.city





