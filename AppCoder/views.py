from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import  authenticate, login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Alumno, Profesor, Curso, Avatar, Entregable
from .forms import AlumnoForm, ProfesorForm, CursoForm, UserEditForm, EntregableForm

# Vistas para el inicio y registro
def inicio(request):
    return render(request, 'inicio.html')

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")
    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario , password=contra)
            if user is not None:
                login(request , user )
                avatares = Avatar.objects.filter(user=request.user.id)
                if avatares:
                    url_avatar = avatares[0].imagen.url
                else:
                    url_avatar = None  # O una URL predeterminada si no hay avatares disponibles
                return render( request , "inicio.html" , {"url": url_avatar})
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")
    form = AuthenticationForm()
    return render( request , "Login.html" , {"form":form})

@login_required
def editar_perfil(request):
   usuario = request.user
   if request.method == "POST":
        
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "inicio.html")

   else:
        miFormulario = UserEditForm(initial={"email":usuario.email})
    
   return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})


# Vista para cerrar sesión
@login_required
def cerrar_sesion(request):
    auth_logout(request)
    return redirect('inicio')

#Verificación
def es_administrador(user):
    return user.is_authenticated and user.is_superuser



# Vistas CRUD para profesores
def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores.html', {'profesores': profesores})

@login_required
def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesores')
    else:
        form = ProfesorForm()
    return render(request, 'agregar_profesor.html', {'form': form})

@login_required
def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('profesores')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'editar_profesor.html', {'form': form})

@login_required
def eliminar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    return redirect('profesores')

# Vistas CRUD para alumnos
def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'alumnos.html', {'alumnos': alumnos})

@login_required
def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'agregar_alumno.html', {'form': form})

@login_required
def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'editar_alumno.html', {'form': form, 'alumno':alumno})

@login_required
def eliminar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect('alumnos')

@login_required
def entregar_entregable(request, entregable_id):
    entregable = Entregable.objects.get(id=entregable_id)

    if request.method == 'POST':
        form = EntregableForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardar la entrega en la base de datos
            entrega = form.save(commit=False)
            entrega.entregable = entregable
            entrega.usuario = request.user
            entrega.save()
            return redirect('detalle_entregable', entregable_id=entregable_id)
    else:
        form = EntregableForm()

    return render(request, 'entregar_entregable.html', {'form': form})
# CRUD para CURSOS

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursos})

def ver_cursos(request):
    cursos = Curso.objects.all()   
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request , "cursos.html", {"url":avatares[0].imagen.url , "cursos": cursos })

def buscar_curso(request):
    if request.method == 'GET' and 'nombre' in request.GET:
        nombre = request.GET.get('nombre', '')
        cursos = Curso.objects.filter(nombre__icontains=nombre)
    else:
        cursos = Curso.objects.all()
    return render(request, 'buscar_curso.html', {'cursos': cursos})

@login_required
def alta_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save()
            texto = f"Se guardó en la BD el curso: {curso.nombre} {curso.camada}"
            return HttpResponse(texto)
    else:
        form = CursoForm()
    return render(request, 'alta_curso.html', {'form': form})

@login_required
def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'editar_curso.html', {'form': form, 'curso': curso})
    
@login_required
def eliminar_curso(request , id ):
    curso = Curso.objects.get(id=id)
    curso.delete()
    cursos = Curso.objects.all()
    return render(request , "cursos.html" , {"cursos":cursos})

# Otras vistas...
def buscar(request):
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains=nombre)
    else:
        cursos = Curso.objects.all()
    return render(request, 'resultado_busqueda.html', {'cursos': cursos})
