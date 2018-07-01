from django.db import models


# Create your models here.

class Licitacion(models.Model):
    nombre = models.CharField(max_length=40)
    VALORES = ((True, 'Si'), (False, 'No'))
    publicada = models.BooleanField(max_length=1, choices=VALORES, default='No')

    def __str__(self):
        return self.nombre


class Contrato(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateTimeField(auto_now_add=True, editable='true')
    licitacion = models.ForeignKey(Licitacion, null='false', blank='false', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateTimeField(auto_now_add=True, editable='false')
    adjunto = models.FileField(upload_to="archivos/", null=True, blank=True)
    contrato = models.ForeignKey(Contrato, null='false', blank='false', on_delete=models.CASCADE)
    licitacion = models.ForeignKey(Licitacion, null='false', blank='false', on_delete=models.CASCADE)
    precio = models.DecimalField(decimal_places=2, max_digits=20)
    iva = models.IntegerField(default=21,editable='false')
    total = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        return self.nombre
