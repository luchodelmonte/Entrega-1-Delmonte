from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader


def vista_saludo(request):
    return HttpResponse("Hola coders! :)")


def iniciar_sesion(request):
    return HttpResponse("Pasame tu username y psw por wpp je")


def dia_hoy(request, nombre):
    hoy = datetime.now()

    respuesta = f"Hoy es {hoy} - Bienvenido {nombre}"
    return HttpResponse(respuesta)


def año_nacimiento(request, edad):
    edad = int(edad)
    año_nac = datetime.now().year - edad
    return HttpResponse(f"Naciste en {año_nac}")


def vista_plantilla(request):
    archivo = open(
        "/Users/lucianodelmonte/Documents/testDjango/proyectocoder/proyectocoder/templates/plantilla.html")
    plantilla = Template(archivo.read())
    archivo.close()
    datos = {"nombre": "Luciano", "fecha": datetime.now(),
             "apellido": "Delmonte"}
    contexto = Context(datos)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


def vista_listado_alumnos(request):
    archivo = open(
        "/Users/lucianodelmonte/Documents/testDjango/proyectocoder/proyectocoder/templates/listado_alumnos.html")
    plantilla = Template(archivo.read())
    archivo.close()
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia",
                       "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante", "Barbara Pino"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}
    contexto = Context(datos)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


def vista_listado_alumnos2(request):
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia",
                       "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante", "Barbara Pino"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}
    plantilla = loader.get_template("listado_alumnos.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)
