from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import Animal, Invertebrado, Vertebrado

def base(request):
    return render(request,"appcoder/base.html")


def inicio(request):
    return render(request,"appcoder/index.html")

def creacion_animal(request):
    if request.method == "POST":
        animal_nombre = request.POST["animal"]
        animal_bioma = request.POST["bioma"]

        animal = Animal(nombre=animal_nombre, bioma=animal_bioma)
        animal.save()

    return render(request, "appcoder/animal_formulario.html")

def desierto(request):
    return render(request, "appcoder/desierto.html")

def pastizal(request):
    return render(request, "appcoder/pastizal.html")

def sabana(request):
    return render(request, "appcoder/sabana.html")

def bosque(request):
    return render(request, "appcoder/bosque.html")

def animales(request):
    return render(request, "appcoder/animales.html")

