from django.contrib.admin import ModelAdmin, register

from rest.app.user.models import User


@register(User)
class CustomUserAdmin(ModelAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "date_joined",
    )
