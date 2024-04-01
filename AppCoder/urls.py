from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name = "home"),
    path("ver_cursos", views.ver_cursos),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("cursos", views.cursos, name="cursos"),
    path("alumnos", views.alumnos, name="alumnos"),
    path("profesores", views.profesores, name="profesores"),
    path("ingresar", views.ingresar, name="ingresar"),
    path("registrar", views.registrar, name="registrar"),
    path("alta_curso", views.curso_formulario, name = "formulario"),
    path("buscar_curso",views.buscar_curso),
    path("buscar",views.buscar),
    path("elimina_curso/<int:id>", views.elimina_curso, name="elimina_curso"),
    path("editar_curso/<int:id>", views.editar, name="editar_curso")
]

