from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import ToDoItem, ToDoList
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import MyRegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_view')
        else:
            pass
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = MyRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def list_view(request):
    lists = ToDoList.objects.filter(user=request.user)
    return render(request, 'list_view.html', {'lists': lists})

@login_required
def list_detail_view(request, list_id):
    list = get_object_or_404(ToDoList, pk=list_id, user=request.user)
    items = ToDoItem.objects.filter(list=list)
    return render(request, 'list_detail_view.html', {'list': list, 'items': items})

@login_required
def create_list_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        list = ToDoList.objects.create(user=request.user, name=name, description=description)
        return redirect('list_detail_view', list_id=list.id)
    else:
        return render(request, 'create_list_view.html')