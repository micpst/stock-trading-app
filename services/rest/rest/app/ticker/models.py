from django.db.models import CASCADE, DateTimeField, DecimalField, ForeignKey, Model

from rest.app.stock.models import Stock


class Ticker(Model):
    """
    Stock price ticker model.
    """

    stock = ForeignKey(to=Stock, on_delete=CASCADE)
    price = DecimalField(max_digits=19, decimal_places=4)
    time_epoch = DateTimeField()

    class Meta:
        db_table = "tbl_ticker"
