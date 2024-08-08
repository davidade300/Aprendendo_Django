from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # return HttpResponse("HOME RECIPE")
    return render(request, "recipes/home.html", context={"name": "David"})


def contato(request):
    return render(request, "recipes/contato.html")


def sobre(request):
    return HttpResponse("sobre")
