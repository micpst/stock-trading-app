from django.db.models import CASCADE, CharField, DecimalField, ForeignKey, Model, TextChoices
from django.utils.translation import gettext_lazy as _


class AccountType(TextChoices):
    STANDARD = "STANDARD", _("Standard")
    PROFESSIONAL = "PROFESSIONAL", _("Professional")
    DEMO = "DEMO", _("Demo")


class AccountStatus(TextChoices):
    ACTIVE = "ACTIVE", _("Active")
    CLOSED = "CLOSED", _("Closed")
    SUSPENDED = "SUSPENDED", _("Suspended")


class AccountCurrency(TextChoices):
    USD = "USD", "USD"
    EUR = "EUR", "EUR"
    PLN = "PLN", "PLN"


class Account(Model):
    """
    User trading account model.
    """

    user = ForeignKey(to="user.User", on_delete=CASCADE, related_name="+")
    type = CharField(max_length=12, choices=AccountType.choices)
    status = CharField(max_length=9, choices=AccountStatus.choices, default=AccountStatus.ACTIVE)
    balance = DecimalField(max_digits=19, decimal_places=4)
    currency = CharField(max_length=3, choices=AccountCurrency.choices)

    class Meta:
        db_table = "tbl_account"
