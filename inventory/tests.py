# inventory/tests.py
from django.test import TestCase
from .models import Item, Unit

class UnitModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створюємо об'єкт складу для тестів
        cls.unit = Unit.objects.create(unitName="Склад №1")

    def test_unit_name(self):
        # Тест на перевірку правильності імені складу
        self.assertEqual(self.unit.unitName, "Склад №1")
    
    def test_unit_str(self):
        # Тест на метод __str__ у моделі unit
        self.assertEqual(str(self.unitName), "Склад №1")

class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створюємо об'єкт складу і товар для тестів
        cls.unit = Unit.objects.create(unitName="Склад №1")
        cls.item = Item.objects.create(
            name="Товар 1",
            inventoryNumber="T001",
            series=10,
            initialCost=30
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

    def test_item_unit(self):
        # Тест на перевірку складу, до якого належить товар
        self.assertEqual(self.item.unit.unitName, "Склад №1")

    def test_item_str(self):
        # Тест на метод __str__ у моделі Item
        self.assertEqual(str(self.item), "Товар 1")
