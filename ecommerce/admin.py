from django.contrib import admin
from ecommerce.models import Product, Payment, Order, Customer, Order_Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


class Order_ProductAdmin(admin.ModelAdmin):
    list_display = ('get_customer_name', 'count', 'price')

    def get_customer_name(self, obj):
        return obj.order.customer.first_name + ' ' + obj.order.customer.last_name



class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_customer_name',)
    #list_filter = ('get_customer_name',)

    def get_customer_name(self, obj):
        return obj.customer.first_name + ' ' + obj.customer.last_name


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

    list_filter = ('first_name', 'last_name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_Product, Order_ProductAdmin)
