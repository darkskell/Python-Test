from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'created']
    list_filter = ['created']
    inlines = [OrderItemInline]

admin.site.register(Order, CustomerAdmin)
