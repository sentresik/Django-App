from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import ToDoItem
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import MyRegistrationForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('your-desired-redirect-url')
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