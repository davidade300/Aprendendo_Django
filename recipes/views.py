from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("HOME RECIPE")


def contato(request):
    return HttpResponse("contato")


def sobre(request):
    return HttpResponse("sobre")
