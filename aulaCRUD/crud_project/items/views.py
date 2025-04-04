from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .form import ItemForm

def item_read(request):
    items = Item.objects.all()
    return render(request, "item_read.html", {'items':items})

def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_read')
        else:
            form = ItemForm

    return render(request, "item_form.html", {'form': form})

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'PUT':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_read')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_read.html')
    return render(request, 'item_confirm_delete.html', {'item': item})