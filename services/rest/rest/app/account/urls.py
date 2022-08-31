from django.urls import path

from rest.app.account.views import AccountDetailsView, AccountSelectView, AccountsListView

urlpatterns = [
    path("", AccountsListView.as_view(), name="accounts_list_create"),
    path("/<int:pk>", AccountDetailsView.as_view(), name="account_retrieve_update_delete"),
    path("/<int:pk>/select", AccountSelectView.as_view(), name="account_select"),
]
