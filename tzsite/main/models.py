from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from ordered_model.models import OrderedModel


# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(OrderedModel):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    task = models.CharField(max_length=300)
    date = models.DateTimeField()
    complete = models.BooleanField()

    def __str__(self):
        return self.task
