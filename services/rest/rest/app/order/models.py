from django.core.validators import MinValueValidator
from django.db.models import CASCADE, CharField, DateTimeField, DecimalField, ForeignKey, Model, PositiveIntegerField, \
    TextChoices
from django.utils.translation import gettext_lazy as _

from rest.app.user.models import User
from rest.app.stock.models import Stock


class Order(Model):
    """
    Abstract order model.
    """

    class OrderType(TextChoices):
        BUY = "B", _("Buy")
        SELL = "S", _("Sell")

    class OrderT(TextChoices):
        LIMIT = "L", _("Limit")
        STOP = "S", _("Stop")
        __empty__ = _("Market")

    class OrderStatus(TextChoices):
        OPEN = "O", _("Open")
        FILLED = "F", _("Filled")
        PARTIALLY_FILLED = "P", _("Partially filled")
        CANCELLED = "C", _("Cancelled")

    user = ForeignKey(to=User, on_delete=CASCADE)
    stock = ForeignKey(to=Stock, on_delete=CASCADE)
    type = CharField(max_length=1, choices=OrderType.choices)
    status = CharField(max_length=1, choices=OrderStatus.choices)
    price = DecimalField(max_digits=19, decimal_places=4)
    volume = PositiveIntegerField(validators=[MinValueValidator(1)])
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tbl_order"
