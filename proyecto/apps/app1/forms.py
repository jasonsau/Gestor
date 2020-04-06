from django import forms
from apps.app1.models import *
from django.contrib.admin.widgets import AdminDateWidget

class MatriculaForm(forms.ModelForm):
	class Meta:
		model = Matricula
		fields = {
			'fecha_matricula',
			'alumno',
			'especialidad_matricula',
			'seccion_matricula',
			'nivel_matricula',
		}
		labels ={
			'fecha_matricula': 'Fecha de Matricula',
			'alumno': 'Nombre de Alumno',
			'especialidad_matricula': 'Especialidad',
			'seccion_matricula': 'Seccion',
			'nivel_matricula': 'Nivel',
		}

class AsignaturaForm(forms.ModelForm):
	class Meta:
		model=Asignatura
		fields={
		'codigo_asignatura',
		'nombre_asignatura',
		}
		labels={
		'codigo_asignatura':'Codigo',
		'nombre_asignatura':'Nombre',
		}


class NotasActividadForm(forms.ModelForm):
	class Meta:
		model = NotasActividad
		fields={
			'id_actividad',
			'valor',
			'id_especialidad',
			'id_asignatura',
			'id_seccion',
			'id_nivel',
			'id_alumno',
			'id_periodo',
		}
		labels={
			'id_actividad': 'Actividad',
			'valor':'Nota',
			'id_especialidad': 'Especialidad',
			'id_asignatura': 'Asignatura',
			'id_seccion': 'Seccion',
			'id_nivel': 'Nivel',
			'id_alumno': 'Alumno',
			'id_periodo':'Periodo',
		}

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User
		fields=('username','password','email')
