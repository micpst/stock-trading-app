from django.db.models import CharField, DecimalField, Model


class Stock(Model):
    """
    Stock company information model.
    """

    ticker = CharField(max_length=10, unique=True)
    company_name = CharField(max_length=255, unique=True)
    market_capitalization = DecimalField(null=True, blank=True, max_digits=19, decimal_places=2)
    dividend_yield = DecimalField(null=True, blank=True, max_digits=19, decimal_places=2)
    eps = DecimalField(null=True, blank=True, max_digits=19, decimal_places=2)
    pe = DecimalField(null=True, blank=True, max_digits=19, decimal_places=2)
    pb = DecimalField(null=True, blank=True, max_digits=19, decimal_places=2)
    de = DecimalField(null=True, blank=True, max_digits=19, decimal_places=2)

    class Meta:
        db_table = "tbl_stock"

    def __str__(self) -> str:
        return self.ticker
