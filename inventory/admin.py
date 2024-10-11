# inventory/admin.py
from django.contrib import admin
from .models import Item, Warehouse

# Базова реєстрація моделей для адміністративного інтерфейсу
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'quantity', 'warehouse')  # Поля для відображення у списку
    search_fields = ('name', 'code')  # Поля для пошуку
    list_filter = ('warehouse',)  # Фільтр за складом
    ordering = ('name',)  # Сортування за назвою

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Відображення назв складів
    search_fields = ('name',)  # Пошук за назвою складу
