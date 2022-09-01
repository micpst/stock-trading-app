from django.urls import path

from rest.app.order.views import OrderCancelView, OrderPlaceView, OrdersListView

urlpatterns = [
    path("", OrdersListView.as_view(), name="orders_list"),
    path("/place", OrderPlaceView.as_view(), name="order_place"),
    path("/<int:pk>/cancel", OrderCancelView.as_view(), name="order_cancel"),
]
