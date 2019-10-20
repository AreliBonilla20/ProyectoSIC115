from django.db import models
from apps.asientos_contables.models import *

class tipoCuenta(models.Model):
    tipo=models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.tipo)

class cuenta(models.Model):
    codigo=models.IntegerField()
    nombre = models.CharField(max_length=50)
    tipo_cuenta=models.ForeignKey(tipoCuenta,null=False,blank=False,on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.nombre)

class asientoContable(models.Model):
    numero_asiento=models.IntegerField()
    fecha=models.DateField()
    cuenta_debe=models.ForeignKey(cuenta,null=False,blank=False,on_delete=models.CASCADE,related_name='cuenta_debe')
    detalle_debe=models.CharField(max_length=150)
    debe=models.DecimalField(max_digits=8,decimal_places=2)
    cuenta_haber=models.ForeignKey(cuenta,null=False,blank=False,on_delete=models.CASCADE,related_name='cuenta_haber')
    detalle_haber=models.CharField(max_length=150)
    haber=models.DecimalField(max_digits=8,decimal_places=2)
    def __str__(self):
        return '{}'.format(self.cuenta_debe.nombre+"-"+self.cuenta_haber.nombre)

class registroTMayor(models.Model):
    cuenta=models.ForeignKey(cuenta,null=False,blank=False,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.cuenta)

class movimiento(models.Model):
    registro=models.ForeignKey(registroTMayor,null=False,blank=False,on_delete=models.CASCADE)
    concepto=models.ForeignKey(cuenta,null=False,blank=False,on_delete=models.CASCADE)
    debe=models.DecimalField(max_digits=8,decimal_places=2)
    haber=models.DecimalField(max_digits=8,decimal_places=2)
    
    def __str__(self):
        return '{}'.format(self.registro)  