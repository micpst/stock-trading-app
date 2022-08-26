from django.urls import path

from rest.app.stock.views import StockDetailsView, StocksListView

urlpatterns = [
    path("", StocksListView.as_view(), name="stocks_list_create"),
    path("/<int:pk>", StockDetailsView.as_view(), name="stock_retrieve_update_delete"),
]
