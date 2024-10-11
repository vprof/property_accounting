# inventory/tests.py
from django.test import TestCase
from .models import Item, Warehouse

class WarehouseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створюємо об'єкт складу для тестів
        cls.warehouse = Warehouse.objects.create(name="Склад №1")

    def test_warehouse_name(self):
        # Тест на перевірку правильності імені складу
        self.assertEqual(self.warehouse.name, "Склад №1")
    
    def test_warehouse_str(self):
        # Тест на метод __str__ у моделі Warehouse
        self.assertEqual(str(self.warehouse), "Склад №1")

class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створюємо об'єкт складу і товар для тестів
        cls.warehouse = Warehouse.objects.create(name="Склад №1")
        cls.item = Item.objects.create(
            name="Товар 1",
            code="T001",
            quantity=10,
            warehouse=cls.warehouse
        )

    def test_item_name(self):
        # Тест на перевірку правильності імені товару
        self.assertEqual(self.item.name, "Товар 1")
    
    def test_item_code(self):
        # Тест на перевірку коду товару
        self.assertEqual(self.item.code, "T001")

    def test_item_quantity(self):
        # Тест на перевірку кількості товару
        self.assertEqual(self.item.quantity, 10)

    def test_item_warehouse(self):
        # Тест на перевірку складу, до якого належить товар
        self.assertEqual(self.item.warehouse.name, "Склад №1")

    def test_item_str(self):
        # Тест на метод __str__ у моделі Item
        self.assertEqual(str(self.item), "Товар 1")
