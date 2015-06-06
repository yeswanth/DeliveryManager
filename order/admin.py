from django.contrib import admin
from order.models import Order, OrderItem, DeliveryBoyOrder, DeliveryBoy 

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

class DeliveryBoyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order,OrderAdmin)
admin.site.register(DeliveryBoy,DeliveryBoyAdmin)
