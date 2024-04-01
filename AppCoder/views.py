from django.shortcuts import render, redirect
from AppCoder.models import Curso
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario
from .forms import EntregableForm



def inicio(request):
    return render( request , "padre.html")



def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)


def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def inicio(request):
    return render(request, 'plantilla.html')

def home(request):
    return render(request, 'home.html')

def cursos(request):
    return render(request, 'cursos.html')

def alumnos(request):
    return render(request, 'alumnos.html')

def profesores(request):
    return render(request, 'profesores.html')

def ingresar(request):
    return render(request, 'ingresar.html')

def registrar(request):
    return render(request, 'registrar.html')

def curso_formulario(request):
    if request.method == "POST":
        
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso(nombre=datos.get("nombre"), camada=datos.get("camada"))
            curso.save()
            return render(request , "formulario.html")

    return render(request , "formulario.html")

def buscar_curso(request):
    return render(request,"buscar_curso.html")


def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre_icontains = nombre)
        return render (request , "resultado_busqueda.html", {"curso": cursos})
    else: 
        return HttpResponse("Ingrese el nombre del curso")
    
def elimina_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html", {"cursos":cursos})

def editar (request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Curso_formulario (request.POST)
        if mi_formulario.is_valid(): 
            datos = mi_formulario.cleanes_data 
            curso.nombre = datos["nombre"]
            curso.camada = datos ["camada"]
            curso.save()

            curso = Curso.objects.all()

            return render (request, "cursos.html", {"cursos":curso})
    else: 
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre, "camada": curso.camada})

    return render (request, "editar_curso.html", {"mi_formulario":mi_formulario, "curso":curso})


def agregar_entregable(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos.html')  
    else:
        form = EntregableForm()
    return render(request, 'agregar_entregable.html', {'form': form})
