from django.db import models
from apps.asientos_contables.models import *

class periodoContable(models.Model):
    fechaInicio=models.DateField()
    fechaFinal=models.DateField()
    estado=models.CharField(default="Abierto",max_length=25)

class tipoCuenta(models.Model):
    tipo=models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.tipo)

class cuenta(models.Model):
    codigo=models.CharField(max_length=25)
    subcuenta=models.CharField(max_length=50, null=True)
    nombre = models.CharField(max_length=50)
    tipo_cuenta=models.ForeignKey(tipoCuenta,null=False,blank=False,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)

class libroDiario(models.Model):
    fecha=models.DateField()
    concepto=models.CharField(max_length=100)
    
    def __str__(self):
        return '{}'.format(self.fecha)  

class asientoContable(models.Model):
    numero_asiento=models.IntegerField()
    libroD=models.ForeignKey(libroDiario,null=False,blank=False,on_delete=models.CASCADE)
    cuenta_debe=models.ForeignKey(cuenta,null=False,blank=False,on_delete=models.CASCADE,related_name='cuenta_debe')
    importeDebe=models.DecimalField(max_digits=8,decimal_places=2)
    cuenta_haber=models.ForeignKey(cuenta,null=False,blank=False,on_delete=models.CASCADE,related_name='cuenta_haber')
    importeHaber=models.DecimalField(max_digits=8,decimal_places=2)
    periodo = models.ForeignKey(periodoContable,null=True,blank=True,on_delete=models.CASCADE)

    
    def __str__(self):
        return '{}'.format(self.cuenta_debe.nombre+"-"+self.cuenta_haber.nombre)

class libroMayor(models.Model):
    nombre_cuenta=models.ForeignKey(cuenta,null=False,blank=False,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre_cuenta)

class elementoMayor(models.Model):
    debe=models.DecimalField(max_digits=8,decimal_places=3)
    haber=models.DecimalField(max_digits=8,decimal_places=3)
    mayor=models.ForeignKey(libroMayor,null=False,blank=False,on_delete=models.CASCADE)
    periodoCont = models.ForeignKey(periodoContable,null=True,blank=True,on_delete=models.CASCADE)

    def _get_saldo(self):
        if self.debe>self.haber:
            return(self.debe-self.haber)
        elif self.haber>self.debe:
            return(self.haber-self.debe)
        else:
            return(self.debe-self.haber)
    saldo = property(_get_saldo)
    
    def _get_montofinal(self):
        
        return(self.debe-self.haber)
        
    monto = property(_get_montofinal)
    
class libroMayores(models.Model):
    mayor=models.ForeignKey(libroMayor,null=False,blank=False,on_delete=models.CASCADE)

class balanceComprobacion(models.Model):
    totalSumaDebe=models.DecimalField(max_digits=8,decimal_places=2)
    totalSumaHaber=models.DecimalField(max_digits=8,decimal_places=2)
 
class elementoBalanceComprobacion(models.Model):
    cuentas=models.ForeignKey(cuenta,null=False,blank=False,on_delete=models.CASCADE)
    sumaDebe=models.DecimalField(max_digits=8,decimal_places=2)
    sumaHaber=models.DecimalField(max_digits=8,decimal_places=2)