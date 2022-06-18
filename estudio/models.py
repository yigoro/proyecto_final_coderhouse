from django.db import models

class Estudio(models.Model):
    universidad = models.CharField(max_length=40)
    anio_inicio = models.IntegerField()
    titulo = models.CharField(max_length=40)
    finalizado = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.universidad} - Inicio: {self.anio_inicio} - Titulo: {self.titulo} - Finalizado: {self.finalizado}'
