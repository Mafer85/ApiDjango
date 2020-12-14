from django.db import models
from django.contrib import admin

class empleado(models.Model):
    usuarios  = models.CharField(max_length=30)
    Contrasenia = models.CharField(max_length=30)
    Roles = models.CharField(max_length=30)

    def __str__(self):
        return self.usuarios

class categoria(models.Model):
    nombre_categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_categoria

class producto(models.Model):
    nombre_producto = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=300)
    Existencia = models.IntegerField()
    Precio = models.FloatField()
    Categoria = models.ForeignKey(
    categoria,  on_delete=models.CASCADE
    )
    def __str__(self):
        return self.nombre_producto


class factura(models.Model):
    Nombre_Cliente = models.CharField(max_length=100)
    Producto = models.ForeignKey(producto,related_name="producto", on_delete=models.CASCADE)
    serie = models.IntegerField()
    nit = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    Fecha = models.DateField()
    total = models.FloatField()

    def __int__(self):
        return self.serie

# Create your models here.
