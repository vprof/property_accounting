from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=255)

class Item(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField(default=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('in', 'Прихід'),
        ('move', 'Переміщення'),
        ('out', 'Списання')
    ]
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    warehouse_from = models.ForeignKey(Warehouse, related_name='warehouse_from', on_delete=models.SET_NULL, null=True, blank=True)
    warehouse_to = models.ForeignKey(Warehouse, related_name='warehouse_to', on_delete=models.SET_NULL, null=True, blank=True)