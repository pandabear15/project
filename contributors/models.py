from django.db import models


class Contributor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30, default='Anonymous')
    val1 = models.IntegerField(default=0)
    val2 = models.IntegerField(default=0)
    val3 = models.IntegerField(default=0)
    # render this in client side
    # clothes = models.IntegerField(default=0)
    books = models.IntegerField(default=0)
    # render this in client side
    # total = models.IntegerField()
    class_of = models.CharField(max_length=6, default='N/A')

    def __str__(self):
        return self.name
