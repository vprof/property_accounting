# inventory/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Warehouse
from .forms import ItemForm
from django.http import HttpResponse

def home(request):
    # Головна сторінка, яка може містити інформацію про склади або загальну статистику
    warehouses = Warehouse.objects.all()
    return render(request, 'inventory/home.html', {'warehouses': warehouses})

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

def warehouse_detail(request, pk):
    # Відображає деталі конкретного складу та перелік товарів на ньому
    warehouse = get_object_or_404(Warehouse, pk=pk)
    items_in_warehouse = Item.objects.filter(warehouse=warehouse)
    return render(request, 'inventory/warehouse_detail.html', {
        'warehouse': warehouse,
        'items': items_in_warehouse
    })

def test_db_connection(request):
    # Створюємо або отримуємо існуючий запис
    warehouse, _ = Warehouse.objects.get_or_create(name="Тестовий склад")

    # Відображаємо підтвердження
    return HttpResponse(f"Підключення успішне: {warehouse.name}")