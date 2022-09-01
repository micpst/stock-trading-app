from django.core.validators import MinValueValidator
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    DecimalField,
    ForeignKey,
    Model,
    PositiveIntegerField,
    TextChoices,
)
from django.utils.translation import gettext_lazy as _

from rest.app.account.models import Account
from rest.app.stock.models import Stock
from rest.common.mixins import UpdateMixin


class OrderType(TextChoices):
    BUY = "BUY", _("Buy")
    SELL = "SELL", _("Sell")


class OrderStatus(TextChoices):
    OPEN = "OPEN", _("Open")
    FILLED = "FILLED", _("Filled")
    PARTIALLY_FILLED = "PARTIALLY_FILLED", _("Partially filled")
    CANCELLED = "CANCELLED", _("Cancelled")


class Order(Model, UpdateMixin):
    """
    Order model.
    """

    account = ForeignKey(to=Account, on_delete=CASCADE)
    stock = ForeignKey(to=Stock, on_delete=CASCADE)
    type = CharField(max_length=4, choices=OrderType.choices)
    status = CharField(max_length=16, choices=OrderStatus.choices)
    price = DecimalField(max_digits=19, decimal_places=4)
    volume = PositiveIntegerField(validators=[MinValueValidator(1)])
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tbl_order"
