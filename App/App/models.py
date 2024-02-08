from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

def get_default_list(user):
    if user:
        try:
            default_list = user.default_todolist
        except AttributeError:
            default_list = ToDoList.objects.create(user=user, name="My First List", description="You can create tasks inside the list!")
            user.default_todolist = default_list
            user.save()
        return default_list
    else:
        return ToDoList.objects.get(name="Default List")

class ToDoList(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

class ToDoItem(models.Model):
    text = models.CharField(max_length=100)
    due_date = models.DateField(default=now)
    is_completed = models.BooleanField(default=False)
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, default=get_default_list)