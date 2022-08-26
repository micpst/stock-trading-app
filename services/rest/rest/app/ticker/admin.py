from django.contrib.admin import ModelAdmin, register

from rest.app.ticker.models import PriceTicker


@register(PriceTicker)
class PriceTickerAdmin(ModelAdmin):
    list_display = (
        "stock",
        "price",
        "time_epoch",
    )
