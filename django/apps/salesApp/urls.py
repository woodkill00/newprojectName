from django.urls import path
from apps.salesApp.views import (
    sales_home_view,
    Sale,
    SaleListView,
    sale_list_view,
    SaleDetailView,
)

app_name = 'salesApp'

urlpatterns = [
    path('', sales_home_view, name='sales_home'),
    path('salesList/', SaleListView.as_view(), name='sales_list'),
    # path('salesList/', sale_list_view, name='sales_list'),
    path('salesDetail/<pk>/', SaleDetailView.as_view(), name='sales_detail'),
]
