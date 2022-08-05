from inspect import Attribute
from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, "index.html")


def projects(request):
    # projects = {'projects' : Project.objects.all()}
    return render(request, "projects.html")

def designs(request):
    context = {'designs' : Design.objects.all()}
    return render(request, "designs.html", context)
