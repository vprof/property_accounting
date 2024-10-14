# inventory/admin.py
from django.contrib import admin
from .models import Item, Unit

# Базова реєстрація моделей для адміністративного інтерфейсу
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'inventoryNumber', 'series', 'expirationDate')  # Поля для відображення у списку
    search_fields = ('name', 'inventoryNumber')  # Поля для пошуку
    list_filter = ('series',)  # Фільтр за складом
    ordering = ('name',)  # Сортування за назвою

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit',)  # Відображення назв складів
    search_fields = ('unit',)  # Пошук за назвою складу
