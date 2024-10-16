# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.item_list, name='item_list'),
    path('items/add/', views.add_item, name='add_item'),
    path('reports/', views.reports, name='reports'),
    path('unit/<int:pk>/', views.unit_detail, name='unit_detail'),
    path('test-db/', views.test_db_connection, name='test_db_connection'),
    path('operations/arrival/', views.operation_arrival, name='operation_arrival'),
    path('operations/transfer/', views.operation_transfer, name='operation_transfer'),
    path('operations/disposal/', views.operation_disposal, name='operation_disposal'),
]
