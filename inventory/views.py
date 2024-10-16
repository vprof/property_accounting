# inventory/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Unit
from .forms import ItemForm, ArrivalForm, TransferForm, DisposalForm 
from django.http import HttpResponse

def home(request):
    # Головна сторінка, яка може містити інформацію про склади або загальну статистику
    units = Unit.objects.all()
    return render(request, 'inventory/home.html', {'units': units})

def item_list(request):
    # Відображає список усіх об'єктів майна
    items = Item.objects.all()
    return render(request, 'inventory/item_list.html', {'items': items})

def add_item(request):
    # Додає новий товар у базу даних
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Переходить до списку товарів після збереження
    else:
        form = ItemForm()
    return render(request, 'inventory/add_item.html', {'form': form})

def reports(request):
    # Логіка для генерації звітів або відображення сторінки
    return render(request, 'inventory/reports/report_pdf.html')

def unit_detail(request, pk):
    unit = get_object_or_404(Unit, id=pk)
    # Отримуємо всі об'єкти Item, де Unit є отримувачем у транзакції
    items_in_unit = Item.objects.filter(transaction__receiver=unit).distinct()
    
    return render(request, 'inventory/unit_detail.html', {'unit': unit, 'items_in_unit': items_in_unit})

def test_db_connection(request):
    # Створюємо або отримуємо існуючий запис
    unit, _ = Unit.objects.get_or_create(unitName="Тестовий склад")

    # Відображаємо підтвердження
    return HttpResponse(f"Підключення успішне: {unit.unitName}")

def operation_arrival(request):
    if request.method == 'POST':
        form = ArrivalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_list')
    else:
        form = ArrivalForm()
    return render(request, 'inventory/operation_arrival.html', {'form': form})

def operation_transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_list')
    else:
        form = TransferForm()
    return render(request, 'inventory/operation_transfer.html', {'form': form})

def operation_disposal(request):
    if request.method == 'POST':
        form = DisposalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_list')
    else:
        form = DisposalForm()
    return render(request, 'inventory/operation_disposal.html', {'form': form})