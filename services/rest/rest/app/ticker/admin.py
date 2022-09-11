from django.contrib.admin import ModelAdmin, register

from rest.app.ticker.models import Ticker


@register(Ticker)
class TickerAdmin(ModelAdmin):
    list_display = (
        "stock",
        "price",
        "time_epoch",
    )
