from django.contrib.admin import ModelAdmin, register

from rest.app.account.models import Account


@register(Account)
class AccountAdmin(ModelAdmin):
    list_display = (
        "user",
        "type",
        "status",
        "balance",
        "currency",
    )
