from django.db import models

from django.contrib import admin

class Alumno(models.Model):
    nombre  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre    = models.CharField(max_length=60)
    Descripcion      = models.CharField(max_length=60)
    alumno   = models.ManyToManyField(Alumno, through='Notas')

    def __str__(self):
        return self.nombre

class Notas (models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

class NotasInLine(admin.TabularInline):
    model = Notas
    extra = 1


class AlumnoAdmin(admin.ModelAdmin):
    inlines = (NotasInLine,)


class MateriaAdmin (admin.ModelAdmin):
    inlines = (NotasInLine,)
