from django.shortcuts import render
from .models import Movie, Session, Ticket, Customer, Staff
from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

TABLES = {
    'movies': Movie,
    'sessions': Session,
    'tickets': Ticket,
    'customers': Customer,
    'staff': Staff,
}

def dashboard(request, table_name):
    model = TABLES.get(table_name)
    if not model:
        return render(request, '404.html', status=404)

    # Витягуємо всі записи таблиці
    records = model.objects.all()
    columns = [field.name for field in model._meta.fields]
    column_count = len(columns) + 1

    return render(request, 'cinema/dashboard.html', {
        'table_name': table_name,
        'records': records,
        'columns': columns,
        'column_count': column_count,
    })

def add_record(request, table_name):
    model = TABLES.get(table_name)
    if not model:
        return render(request, '404.html', status=404)

    # Автоматично створюємо форму на основі моделі
    Form = modelform_factory(model, exclude=[])
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_table', table_name=table_name)
    else:
        form = Form()

    return render(request, 'cinema/form.html', {'form': form, 'table_name': table_name, 'action': 'Додати запис'})

def edit_record(request, table_name, pk):
    model = TABLES.get(table_name)
    if not model:
        return render(request, '404.html', status=404)

    record = get_object_or_404(model, pk=pk)
    Form = modelform_factory(model, exclude=[])
    if request.method == 'POST':
        form = Form(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('view_table', table_name=table_name)
    else:
        form = Form(instance=record)

    return render(request, 'cinema/form.html', {'form': form, 'table_name': table_name, 'action': 'Редагувати запис'})

def delete_record(request, table_name, pk):
    model = TABLES.get(table_name)
    if not model:
        return render(request, '404.html', status=404)

    record = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('view_table', table_name=table_name)

    return render(request, 'cinema/confirm_delete.html', {'record': record, 'table_name': table_name})

def index(request):
    tables = [
        {'name': 'Movies', 'url': 'view_table', 'args': 'movies'},
        {'name': 'Sessions', 'url': 'view_table', 'args': 'sessions'},
        {'name': 'Tickets', 'url': 'view_table', 'args': 'tickets'},
        {'name': 'Customers', 'url': 'view_table', 'args': 'customers'},
        {'name': 'Staff', 'url': 'view_table', 'args': 'staff'},
    ]
    return render(request, 'cinema/index.html', {'tables': tables})