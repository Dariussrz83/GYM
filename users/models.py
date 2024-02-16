from django.db import models



class Usuario(models.Model):
    nombre = models.CharField('Nombre', blank=False, max_length=100)
    apellido = models.CharField('Apellido',blank=False, max_length=100)
    email = models.EmailField('Correo electronico',blank=False, max_length=250, unique=True)
    dni = models.CharField('Numero de documento', primary_key=True, blank=False, max_length=250, unique=True)
    celular = models.CharField('Celular',blank=False, max_length=250, unique=True)

    def __str__(self):
        texto = '{0} {1} ({2})'
        return texto.format(self.nombre, self.apellido, self.dni,self.celular)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Cuota(models.Model):
    MESES_CHOICES = [
        ('01', 'Enero'),
        ('02', 'Febrero'),
        ('03', 'Marzo'),
        ('04', 'Abril'),
        ('05', 'Mayo'),
        ('06', 'Junio'),
        ('07', 'Julio'),
        ('08', 'Agosto'),
        ('09', 'Septiembre'),
        ('10', 'Octubre'),
        ('11', 'Noviembre'),
        ('12', 'Diciembre'),
    ]

    PAGO_CHOICES = [
        ('01', 'Efectivo'),
        ('02', 'Mercado Pago')
    ]
    socio = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mes = models.CharField(max_length=2, choices=MESES_CHOICES)
    fecha = models.DateField()
    al_dia = models.BooleanField(default=False)
    metodo = models.CharField(max_length=2, choices=PAGO_CHOICES, blank=True, null=True)
    
