from django.shortcuts import render
from django.views.generic import ListView
from .models import ToDoItem
from django.http import HttpResponse


# Create your views here.
class AllToDos(ListView):
    model = ToDoItem
    template_name = "index.html"


# def index(request): #new
#     return HttpResponse('<h1>Django Include URLs</h1>')
