# views.py
import datetime
from ordered_model.models import OrderedModel
import django.http
from django.shortcuts import render

from .models import ToDoList, Item
# Create your views here.
from .forms import CreateNewList
from django.http import HttpResponse, HttpResponseRedirect


def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    checkID = response.POST.getlist('checked')
                    #ls.filter(id__in=checkID).update(checked=True, checkedUser=response.user)
                    #item.delete()
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                        item.bottom()
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(task=txt, complete=False, date=datetime.datetime.now())
                else:
                    print("invalid")

        return render(response, "main/list.html", {"ls": ls})

    return render(response, "main/home.html", {})


def home(response):
    return render(response, "main/home.html", {})


def view(response):
    return render(response, "main/view.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

            return HttpResponseRedirect("/%i" % t.id)

    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form": form})
