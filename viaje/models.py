from django.db import models

class Viaje(models.Model):
    destino = models.CharField(max_length=40)
    nro_vuelo = models.IntegerField()
    fecha = models.DateField()
    notas = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.destino}  - Vuelo: {self.nro_vuelo} - Fecha: {self.fecha} - Notas: {self.notas}'
