from django.urls import path
from appcoder.views import *

urlpatterns = [
    path("inicio/pagina-inicio", inicio, name="coder-inicio"),
    path("desierto/", desierto, name="coder-desierto"),
    path("pastizal/", pastizal, name="coder-pastizal"),
    path("sabana/", sabana, name="coder-sabana"),
    path("bosque/", bosque, name="coder-bosque"),
    path("animales/", animales, name="coder-animales"),
    path("animal/crear/", creacion_animal, name="coder-animal-crear"),
]
