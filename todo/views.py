from django.shortcuts import render, redirect
from .models import Items

# Create your views here.


def todo(request):
    items = Items.objects.all()
    context = {
        "items": items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == "POST":
        name = request.POST.get('item_name')
        done = 'item_done' in request.POST
        Items.objects.create(name=name, done=done)
        return redirect("todo")
    return render(request, 'todo/add_item.html')
    