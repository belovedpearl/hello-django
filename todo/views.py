from django.shortcuts import render
from .models import Items

# Create your views here.


def todo(request):
    items = Items.objects.all()
    context = {
        "items": items
    }
    return render(request, 'todo/todo_list.html', context)