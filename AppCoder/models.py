from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    duracion_horas = models.IntegerField()


    def __str__(self):
        return f"Nombre: {self.nombre}    Camada: {self.camada}"

class Estudiante(models.Model):
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
