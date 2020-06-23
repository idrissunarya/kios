from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    price = models.IntegerField(max_length=10)
    image = models.ImageField(upload_to='product_upload', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name
