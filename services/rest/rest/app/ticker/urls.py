from django.urls import path

from rest.app.ticker.views import TickersListView

urlpatterns = [
    path("", TickersListView.as_view(), name="tickers_list"),
]
