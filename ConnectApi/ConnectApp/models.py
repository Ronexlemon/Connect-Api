from django.db import models

# Create your models here.
class Products(models.Model):
    productName = models.CharField(max_length=255)
    productDescription = models.CharField(max_length=255)
    productImageUrl = models.URLField(max_length=10000)
    productPrice = models.FloatField(max_length=100)

    def __str__(self):
        return self.productName


