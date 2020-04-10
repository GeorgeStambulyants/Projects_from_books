from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from .models import Item, List
from lists.forms import ItemForm


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, id):
    list_ = List.objects.get(id=id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)
    return render(
        request,
        'list.html',
        context={
            'list': list_,
            'form': form,
        }
    )


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    return render(request, 'home.html', {'form': form})
