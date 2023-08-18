from django.contrib import admin
from .models import  Product, Category, Order, OrderItem

# Register your models here.


admin.site.register(Product)
admin.site.register(Category)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'order_date', 'total_price', 'get_status_display']
    list_filter = ['user', 'order_date', 'status']
    search_fields = ['user__username']

    def get_status_display(self, obj):
        return obj.get_status_display()

    get_status_display.admin_order_field = 'status'
    get_status_display.short_description = 'Status'


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity', 'item_price']
    list_filter = ['order', 'product']
    search_fields = ['order__user__username', 'product__name']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)


