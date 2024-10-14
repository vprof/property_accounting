# inventory/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Unit
from .forms import ItemForm
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
    # Відображає деталі конкретного складу та перелік товарів на ньому
    unit = get_object_or_404(Unit, pk=pk)
    items_in_unit = Item.objects.filter(unit=unit)
    return render(request, 'inventory/unit_detail.html', {
        'unit': unit,
        'items': items_in_unit
    })

def test_db_connection(request):
    # Створюємо або отримуємо існуючий запис
    unit, _ = Unit.objects.get_or_create(unit="Тестовий склад")

    # Відображаємо підтвердження
    return HttpResponse(f"Підключення успішне: {unit.unit}")