from django.contrib.admin import ModelAdmin, register

from rest.app.order.models import Order


@register(Order)
class OrderAdmin(ModelAdmin):
    list_display = (
        "user",
        "stock",
        "type",
        "price",
        "volume",
        "status",
        "created_at",
    )
