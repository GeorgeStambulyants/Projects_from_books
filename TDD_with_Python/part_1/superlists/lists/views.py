from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from .models import Item, List
from lists.forms import ItemForm, ExistingListItemForm


User = get_user_model()


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm(), 'user': request.user})


def view_list(request, id):
    list_ = List.objects.get(id=id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
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
        list_ = List()
        list_.owner = request.user
        list_.save()
        form.save(for_list=list_)
        return redirect(list_)
    return render(request, 'home.html', {'form': form})


def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})