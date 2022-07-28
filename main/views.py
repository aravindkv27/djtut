from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(response, id):
    to = ToDoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" %to.name)

# def index_name(response, name):
#     to1 = ToDoList.objects.get(name=name)
#     return HttpResponse("<h1>%s</h1>" %to1.name)

# To get both todolist and item
def index_name(response, name):
    to1 = ToDoList.objects.get(name=name)
    item = to1.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(to1.name, str(item.text)))

# def homepage(response):
#     return HttpResponse("<h1>This is an Homepage</h1>")