from django.contrib import admin
from .models import ToDoItem, ToDoList

# Register your models here.

#@admin.register(ToDoItem)
#class ToDoItemAdmin(admin.ModelAdmin):
#   item_display = ('text', 'due_date' , 'is_completed', 'list_id')  # Example fields

#@admin.register(ToDoList)
#class ToDoItemAdmin(admin.ModelAdmin):
#    list_display = ('name', 'user' , 'description')  # Example fields
