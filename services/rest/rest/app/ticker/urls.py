from django.urls import path

from rest.app.ticker.views import PriceTickersListView

urlpatterns = [
    path("", PriceTickersListView.as_view(), name="price_tickers_list"),
]
