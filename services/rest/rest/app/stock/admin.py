from django.contrib.admin import ModelAdmin, register

from rest.app.stock.models import Stock


@register(Stock)
class StockAdmin(ModelAdmin):
    list_display = (
        "ticker",
        "company_name",
        "market_capitalization",
        "dividend_yield",
        "eps",
        "pe",
        "pb",
        "de",
    )
