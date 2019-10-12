from django.db import models
from apps.asientos_contables.models import *

class cuenta(models.Model):
    codigo=models.IntegerField()
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)


class asientoContable(models.Model):
    fecha=models.DateField()
    detalle=models.CharField(max_length=150)
    importeDebe = models.DecimalField(max_digits=8,decimal_places=2)
    importeHaber = models.DecimalField(max_digits=8,decimal_places=2)
    cuentas=models.ForeignKey(cuenta,null=False,blank=False,on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.fecha,self.detalle,self.importeDebe,self.importeHaber,self.cuentas)

class libroMayor(models.Model):
    numero_folio=models.IntegerField()
    cuentaM=models.ForeignKey(cuenta,null=False,blank=False,on_delete=models.CASCADE)
    total_debe=models.DecimalField(max_digits=8,decimal_places=2)
    total_haber=models.DecimalField(max_digits=8,decimal_places=2)
    def __str__(self):
        return '{}'.format(self.asientoM,self.libro_ppalM)
