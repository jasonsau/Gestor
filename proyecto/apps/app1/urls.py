from django.urls import path, include
from apps.app1.views import *
from django.contrib.auth.decorators import login_required

app_name='gestor'


urlpatterns=[
	#Url para el menu de inicio
	path('index/',login_required(index), name = 'index'),

	#Url para el registro de los alumno 
	path('registro/', login_required(registro), name = "registro"),
	path('registroalumno/',crearAlumno, name = "registro_alumno"),

	#Url para la consulta de alumno segun su NIE
	path('consultaalumno/', login_required(consulta_alumno), name = "consulta_alumno"),
	path('busquedaalumnoa/', ConsultaAlumnoA, name = "consulta_alumnoa"),
	path('editaralumno/<pk>/',editarAlumno.as_view(), name = "editar_alumno"),

	#Url para la consulta de los alumnos por medio de la especialidad, seccion y nivel
	path('consultaseccion/',login_required(ConsultaEspecialidad), name = "consulta_secciona"),
	path('consultaespecialidad/',consultaespecialidad, name = "consulta_especialidad"),

	#Url para el registro de notas de cada actividad
	path('registronotas/', login_required(registronota), name = "registro_nota"),
	path('registroconsulta/', registroconsulta, name = "registro_consulta"),
	path('prueba/<id>/', prueba, name = "prueba"),
	path('pruebaextendido/', pruebaextendido, name= "pruebaextendido"),
	path('modificarnotas/<int:pk>/', modificarNotas, name = "modificar_notas"),

	#Url para la consulta de notas 
	path('consultarnotas/', login_required(ConsultaNotas), name = "consulta_notas"),
	path('consutamostrar/', NotasMostrar, name = "notas_mostrar"),

	#Url para la creacion de asignatura
	path('crearasignatura/', login_required(crearAsignatura.as_view()), name = "crear_asignatura" ),
	path('gestionasignatura/', login_required(listadoAsignatura.as_view()), name = "gestion_asignatura"),
	path('modificarasignatura/<pk>/', login_required(editarAsignatura.as_view()), name = "editar_asignatura"),
	path('eliminarasignatura/<pk>/', eliminarAsignatura.as_view(), name = "eliminar_asignatura"),
]