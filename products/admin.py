from django.contrib import admin

from products.models import ProductCategory, Product 
# регитрация своих моделей что бы они отоброжались
admin.site.register(Product)
admin.site.register(ProductCategory)