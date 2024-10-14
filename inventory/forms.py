# inventory/forms.py
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'inventoryNumber', 'series', 'expirationDate']  # Поля, які будуть відображені у формі
