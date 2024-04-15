from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    curso = {nombre,camada}
    duracion_horas = models.IntegerField()


    def __str__(self):
        return f"Nombre: {self.nombre}    Camada: {self.camada}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Entregable(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_entrega = models.DateField()
    archivo = models.FileField(upload_to='entregables/')

    def __str__(self):
        return self.nombre

class Entrega(models.Model):
    entregable = models.ForeignKey(Entregable, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='entregas/')
    comentario = models.TextField()
    fecha_entrega = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entrega de {self.entregable.nombre} por {self.usuario.username}"
    
class Avatar(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to="avatares" , null=True, blank=True)

    def __str__(self):
        return f"User: {self.user} - Imagen: {self.imagen} "