from django.db import models
from datetime import date
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver

class Encargado(models.Model):
	dui = models.IntegerField(primary_key = True, null = False)
	nombre_encargado = models.CharField(max_length = 200, null = False)
	direcion = models.CharField(max_length = 200, null = False)
	parentescto = models.CharField(max_length = 50, null = False)
	
	def __str__(self):
		return self.nombre_encargado

class Alumno(models.Model):
	nie = models.IntegerField(primary_key = True, null= False)
	nombre_alumno = models.CharField(max_length = 50, null = False)
	apellidos_alumno = models.CharField(max_length = 50, null = False)
	direccion = models.CharField(max_length = 200, null = False)
	fecha_nacimiento = models.DateField(null = False)
	encargado = models.ForeignKey(Encargado, on_delete = models.CASCADE)

	def __str__(self):
		return self.nombre_alumno

class Seccion(models.Model):
	id_seccion = models.IntegerField(primary_key = True, null = False)
	nombre_secion = models.CharField(max_length = 50, null = False)
	cantidad = models.IntegerField(null = False)

	def __str__(self):
		return self.nombre_secion

class Nivel(models.Model):
	id_nivel = models.IntegerField(primary_key = True, null = False)
	nombre_nivel = models.CharField(max_length = 50, null = False)

	def __str__(self):
		return self.nombre_nivel

class Especialidad(models.Model):
	codigo_especialidad = models.CharField(primary_key = True, max_length = 10 ,null = False)
	nombre_especialidad = models.CharField(max_length = 50, null = False)

	def __str__(self):
		return self.nombre_especialidad

class Asignatura(models.Model):
	codigo_asignatura = models.CharField(primary_key = True, max_length = 10, null = False)
	nombre_asignatura = models.CharField(max_length = 50, null = False)

	def __str__(self):
		return self.nombre_asignatura

class Modulo(models. Model):
	codigo_modulo = models.CharField(max_length = 10, null = False)
	nombre_modulo = models.CharField(max_length = 30, null = False)

	def __str__(self):
		return self.nombre_modulo

class Actividad(models.Model):
	id_actividad = models.IntegerField(primary_key = True, null = False)
	nombre_actividad = models.CharField(max_length = 30, null = False)
	porcentaje = models.DecimalField(max_digits = 10, decimal_places = 2)

	def __str__(self):
		return self.nombre_actividad

class Periodo(models.Model):
	id_periodo = models.IntegerField(primary_key = True, null = False)
	nombre_periodo = models.CharField(max_length = 30, null = False)

	def __str__(self):
		return self.nombre_periodo

class Matricula(models.Model):
	fecha_matricula = models.DateField(null = False)
	alumno = models.OneToOneField(Alumno, on_delete = models.CASCADE, null = False)
	especialidad_matricula = models.ForeignKey(Especialidad, on_delete = models.CASCADE, blank = True, null = True)
	seccion_matricula = models.ForeignKey(Seccion, on_delete = models.CASCADE, blank = True, null = True)
	nivel_matricula = models.ForeignKey(Nivel, on_delete = models.CASCADE, blank = True, null = True)

	class Meta:
		ordering = ['-alumno']


class Especialidad_Asignatura(models.Model):
	asignatura = models.ForeignKey(Asignatura, on_delete = models.CASCADE)
	especialidad = models.ForeignKey(Especialidad, on_delete = models.CASCADE)
	nivel = models.ForeignKey(Nivel, on_delete = models.CASCADE)
	modulo = models.ForeignKey(Modulo, on_delete = models.CASCADE, null = True, blank = True)
	
	def __str__ (self):
		return '{0}({1})'.format(self.especialidad, self.asignatura)


class Promedio(models.Model):
	id_promedio = models.IntegerField(primary_key = True, null = False)
	valor_promedio = models.DecimalField(max_digits = 10, decimal_places = 2)
	def __str__(self):
		return self.id_promedio

class NotasActividad(models.Model):
	id_especialidad = models.ForeignKey(Especialidad, on_delete = models.CASCADE)
	id_asignatura = models.ForeignKey(Asignatura, on_delete = models.CASCADE)
	id_actividad = models.ForeignKey(Actividad, on_delete = models.CASCADE)
	id_periodo = models.ForeignKey(Periodo, on_delete =models.CASCADE)
	id_alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
	id_nivel = models.ForeignKey(Nivel, on_delete = models.CASCADE)
	id_seccion = models.ForeignKey(Seccion, on_delete = models.CASCADE)
	valor = models.FloatField()

	class Meta:
		ordering = ['-id_alumno']

