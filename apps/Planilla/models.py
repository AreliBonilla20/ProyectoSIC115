from django.db import models

class Empleado(models.Model):
    
    nombres = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    dui = models.CharField(max_length=10, blank=True, null=True)
    nit = models.CharField(max_length=18, blank=True, null=True)
    nup = models.CharField(max_length=20, blank=True, null=True)
    fechaNacimiento = models.DateField( auto_now=False, auto_now_add=False,blank=True, null=True)
    isss = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        cadena = self.apellidos + ' ' + self.nombres 
        return cadena


class Contrato(models.Model):
    
    empleado = models.ForeignKey('Planilla.Empleado', related_name='Empleado', on_delete=models.CASCADE)
    salario = models.ForeignKey('Planilla.Salario', related_name='Salario', on_delete=models.CASCADE)
    fechaContratacion = models.DateField(auto_now=False, auto_now_add=False)
    cargo = models.ForeignKey("Planilla.Cargo", related_name='Cargo', on_delete=models.CASCADE)

    class Meta:

        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'

    def __str__(self):
        #return f'{self.empleado}/{self.cargo}/{self.salario}'
        return '{}/{}/{}'.format(self.empleado,self.cargo,self.salario)

class Cargo(models.Model):

    nombreCargo = models.CharField(max_length=100, blank=True, null=True)
    gerencia = models.CharField(max_length=100, choices=(('ti','TI'),('ventas','Ventas'),('contabilidad','Contabilidad'),('operaciones','Operaciones')) , blank=True, null=True)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        #return f'{self.nombreCargo}'
        return '{}'.format(self.nombreCargo)


class Salario(models.Model):
    haberBase = models.DecimalField('Haber Base', max_digits=8, decimal_places=2,blank=True, null=True)
    porcISSS = models.DecimalField('Porcentaje descuento ISSS', max_digits=8, decimal_places=2,blank=True, null=True)
    porcAFP = models.DecimalField('Porcentaje descuento AFP', max_digits=8, decimal_places=2,blank=True, null=True)
    bonoAntig = models.DecimalField('Bono de Antiguedad', max_digits=8, decimal_places=2,blank=True, null=True)
    renta = models.DecimalField(("Retencio de renta"), max_digits=8, decimal_places=2,blank=True, null=True)  
    sueldoNeto = models.DecimalField(("Sueldo Neto"), max_digits=8, decimal_places=2,blank=True, null=True) #Total Ganado, Liquido 
    sueldoBruto = models.DecimalField(("Sueldo Bruto"), max_digits=8, decimal_places=2,blank=True, null=True)
    otrosDescuentos = models.DecimalField(("Otros Descuentos"), max_digits=8, decimal_places=2,blank=True, null=True)

    class Meta:
        verbose_name = 'Salario'
        verbose_name_plural = 'Salarios'

    def __str__(self):
        #return f'{self.haberBase}'
        return '{}'.format(self.haberBase)

