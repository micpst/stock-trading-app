from django.urls import path

from rest.app.order.views import OrderDetailsView, OrdersListView

urlpatterns = [
    path("", OrdersListView.as_view(), name="orders_list_create"),
    path("/<int:pk>", OrderDetailsView.as_view(), name="order_retrieve_update_delete"),
]
