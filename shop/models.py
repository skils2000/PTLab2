from django.db import models

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)

class Purchase(models.Model):
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

class ProductToPurchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    finalPrice = models.PositiveIntegerField()
