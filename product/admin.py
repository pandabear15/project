from django.contrib import admin

from .models import Product, Clothes, Other

admin.site.register(Product)
admin.site.register(Clothes)
admin.site.register(Other)