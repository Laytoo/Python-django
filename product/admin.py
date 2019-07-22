from django.contrib import admin

# Register your models here.
from product.models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display =('title','category','status')
    list_filter =('category','status')

admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
