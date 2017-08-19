from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name


class Clothes(models.Model):
    product = models.ManyToManyField(Product)
    internal_description = models.CharField(max_length=20)
    description = models.TextField()
    number = models.IntegerField()
    condition = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    size = models.IntegerField()
    year = models.IntegerField()
    price_in_cents = models.IntegerField() #In cents

    def __str__(self):
        return str(self.id) + ": " + self.internal_description


class Other(models.Model):
    product = models.ManyToManyField(Product)
    internal_description = models.CharField(max_length=20)
    description = models.TextField()
    number = models.IntegerField()
    condition = models.CharField(max_length=15)
    year = models.IntegerField()
    price_in_cents = models.IntegerField()  # In cents

    def __str__(self):
        return str(self.id) + ": " + self.internal_description