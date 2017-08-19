from django.db import models

from product.models import Clothes, Other


class ClothesOrder(models.Model):
    description = models.CharField(max_length=30)
    product_ID = models.IntegerField()
    item_type = models.CharField(max_length=20)
    quantity = models.IntegerField()
    person = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    item = models.ForeignKey(Clothes)

    def __str__(self):
        return self.item_type + "-" + str(self.product_ID) + ": " + self.description + " - Quantity: " + str(self.quantity)


class OtherOrder(models.Model):
    description = models.CharField(max_length=30)
    product_ID = models.IntegerField()
    item_type = models.CharField(max_length=20)
    quantity = models.IntegerField()
    person = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    item = models.ForeignKey(Other)

    def __str__(self):
        return self.item_type + "-" + str(self.product_ID) + ": " + self.description + " - Quantity: " + str(self.quantity)