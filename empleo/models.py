from django.db import models

class Empleo(models.Model):
    empresa = models.CharField(max_length=30)
    periodo = models.IntegerField()
    puesto = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.empresa} - Periodo: {self.periodo} - Puesto: {self.puesto}'
