# inventory/forms.py
from django import forms
from .models import Item, Transaction

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'inventoryNumber', 'series', 'expirationDate']  # Поля, які будуть відображені у формі

class ArrivalForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['item', 'receiver', 'amount', 'price', 'party']
        labels = {'receiver': 'Основний склад'}

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['item', 'sender', 'receiver', 'amount', 'party']
        labels = {'sender': 'Звідки', 'receiver': 'Куди'}

class DisposalForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['item', 'sender', 'amount', 'party']
        labels = {'sender': 'Склад для списання'}