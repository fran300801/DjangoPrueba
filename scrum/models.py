from django.db import models

# Create your models here.

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id} {self.nombre}'

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id} {self.nombre}'

class Programador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    etiqueta = models.ManyToManyField(Etiqueta,blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.nombre}'

    class Meta:
        verbose_name = "Programador"
        verbose_name_plural = "Programadores"

class Sprint(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id} {self.fecha_inicio} {self.fecha_fin}'

class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    completa = models.BooleanField(default=False)
    sprint = models.ForeignKey(Sprint,on_delete=models.CASCADE, blank=True, null=True)
    programador = models.ForeignKey(Programador,on_delete=models.CASCADE, blank=True, null=True)
    etiqueta = models.ManyToManyField(Etiqueta,blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.nombre}'
