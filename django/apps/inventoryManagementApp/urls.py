from django.urls import path
from apps.inventoryManagementApp import views

app_name = 'inventoryManagementApp'

urlpatterns = [
    path('stock/', views.StockListView.as_view(), name='stock-list'),
    # path('stockLookup/<str:pk>/', views.stock_search, name="stock-search"),
    path('stock/create_item/', views.StockItemCreateView.as_view(), name='stock-create-item'),
    path('stock/<int:pk>/update_item/', views.StockItemUpdateView.as_view(), name='stock-update-item'),
    path('stock/<int:pk>/delete_item/', views.StockItemDeleteView.as_view(), name='stock-delete-item'),
]