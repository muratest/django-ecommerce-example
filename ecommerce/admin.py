from django.contrib import admin
from ecommerce.models import Product, Payment

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)



admin.site.register(Product, ProductAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
