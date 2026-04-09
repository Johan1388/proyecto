from django.db import models
from django.contrib.auth.models import User


class AreaVocacional(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Carrera(models.Model):

    TIPOS_FORMACION = [
        ("Tecnico", "Técnico"),
        ("Tecnologo", "Tecnólogo"),
        ("Curso", "Curso Complementario"),
    ]

    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPOS_FORMACION, default="Tecnico")
    area = models.ForeignKey(AreaVocacional, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class Pregunta(models.Model):
    texto = models.TextField()
    area = models.ForeignKey(AreaVocacional, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto


# nuevo modelo 
class Resultado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.ForeignKey(AreaVocacional, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.area.nombre}"