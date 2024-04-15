from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.inicio, name="home"),
    path("buscar", views.buscar),
    path("registro", views.registro, name="registro"),
    path("login/", views.login_request, name="Login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("logout/", views.cerrar_sesion, name="logout"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("editar_perfil", views.editar_perfil, name="editar_perfil"),

#CURSOS    
    path("ver_cursos", views.ver_cursos),
    path("cursos", views.cursos, name="cursos"),
    path("alta_curso", views.alta_curso, name="alta_curso"),
    path("buscar_curso", views.buscar_curso),    
    path("eliminar_curso/<int:id>" , views.eliminar_curso , name="eliminar_curso"),
    path('editar_curso/<int:id>', views.editar_curso, name='editar_curso'),

#PROFESORES
    path("profesores", views.listar_profesores, name="profesores"),
    path("agregar_profesor", views.agregar_profesor, name="agregar_profesor"),
    path('eliminar_profesor/<int:id>', views.eliminar_profesor, name='eliminar_profesor'),
    path('editar_profesor/<int:id>', views.editar_profesor, name='editar_profesor'),
#ALUMNOS
    path("alumnos/", views.ver_alumnos, name="alumnos"),
    path("agregar_alumno/", views.agregar_alumno, name="agregar_alumno"),
    path('eliminar_alumno/<int:id>', views.eliminar_alumno, name='eliminar_alumno'),
    path('editar_alumno/<int:id>', views.editar_alumno, name='editar_alumno'),
    path('entregar/<int:entregable_id>/', views.entregar_entregable, name='entregar_entregable'),
]