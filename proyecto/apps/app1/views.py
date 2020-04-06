from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import *
from django.http import HttpResponseRedirect
from django.core import serializers
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def consultalistas():
	especialidad = Especialidad.objects.all()
	seccion = Seccion.objects.all()
	nivel = Nivel.objects.all()
	
	dic = {'especialidad': especialidad, 'nivel': nivel, 'seccion': seccion}
	return dic

#Funcion para el menu de inicio
def index(request):
	return render(
		request,
		'base/base.html',
		)

#Vista para la vista de la matricula del alumno
def registro(request):
	context = consultalistas()
	return render(request, 'app1/registroAlumno.html', context)

#Vista para guardar la matricula del alumno
def crearAlumno(request):
	if request.method == 'POST':
		#Lectura de los datos mediante el metodo post
		fecha_matricula = request.POST['fechamatricula']
		especialidad = request.POST['especialidad']
		seccion = request.POST['seccion']
		nivel = request.POST['nivel']
		nie = request.POST['nie']
		nombre_alumno = request.POST['nombre_alumno']
		apellidos_alumno = request.POST['apellidos_alumno']
		direccion_alumno = request.POST['direccion_alumno']
		fecha_nacimiento = request.POST['fechanacimiento']
		dui = request.POST['dui']
		nombre_encargado = request.POST['nombre_encargado']
		direccion_encargado = request.POST['direccion_encargado']
		parentesco = request.POST['parentesco']

		#Obtengo las instancias para poder ingresarlas en la entidad matricula
		espe = Especialidad.objects.get(codigo_especialidad = especialidad)
		secc = Seccion.objects.get(id_seccion = seccion)
		ni =Nivel.objects.get(id_nivel = nivel)

		#Crea y guarda la entindad encargado alumno y matricula
		encargado = Encargado(nombre_encargado=  nombre_encargado, dui = dui, direcion = direccion_encargado, parentescto = parentesco)
		encargado.save()
		alumno = Alumno(nie = nie, nombre_alumno = nombre_alumno, apellidos_alumno = apellidos_alumno, encargado = encargado, direccion=direccion_alumno, fecha_nacimiento=fecha_nacimiento)
		alumno.save()
		matricula = Matricula(fecha_matricula= fecha_matricula, alumno = alumno, especialidad_matricula = espe, seccion_matricula=secc, nivel_matricula = ni)
		matricula.save()
		
		return render (
			request, 'app1/consulta_alumno.html',
			)

#Funcion para la vista de consultar a los alumnos segun su especialidad seccion y nivel
def consultaespecialidad(request):
	dic = consultalistas()
	print(dic)
	return render(
		request,
		'app1/consulta_seccion.html',
		dic
		)

#Funcion para la consulta sql y retornar la consulta 
def ConsultaEspecialidad(request):
	if request.method =='POST':
		especialidad = request.POST['especialidad']
		seccion = request.POST['seccion']
		print(especialidad)
		nivel = request.POST['nivel']
		matricula = Matricula.objects.filter(especialidad_matricula = especialidad).filter(nivel_matricula = nivel).filter(seccion_matricula=seccion)
		context={'matricula': matricula}
		return render(request, 'app1/consulta_seccion.html', context)


#Funcion para la vista de la consulta sql de la informacion del alumno
def ConsultaAlumnoA(request):
	nie=request.POST['nie']
	if request.method == 'POST':
		alumno = Alumno.objects.filter(nie = nie)
		matricula=Matricula.objects.filter(alumno__nie = nie)
		context={'alumno':alumno, 'matricula':matricula}
		return render(request,'app1/consulta_alumno.html', context)

#Funcion para la vista de la consulta informacion del alumno 
def consulta_alumno(request):
	return render(
		request,
		'app1/consulta_alumno.html',
		)

#Funcion para el registro de un nuevo usuario 
def register(request):
	registered=False
	if request.method=='POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			login(request,user)
			registered=True
			return redirect('gestor:index')
		else:
			print(user_form.errors)
	else:
		user_form=UserForm()
		return render(request,'registration/register.html',{
			'user_form':user_form,'registered':registered})

#Registro de notas
def prueba(request, id = None):
	ma = Matricula.objects.get(id=id)
	asignatura = Asignatura.objects.all()
	periodo = Periodo.objects.all()
	context= {'ma': ma, 'asignatura': asignatura, 'periodo': periodo}
	return render(
		request,
		'app1/registro_estendido.html', context,
		)

#Guardando y creando registro de notas
def pruebaextendido(request):
	#Lectura de lo datos por medio del post
	nie = request.POST['nie']
	print (nie)
	especialidad = request.POST['especialidad']
	print(especialidad)
	seccion = request.POST['seccion']
	print(seccion)
	nivel = request.POST['nivel']
	print(nivel)
	periodo = request.POST['periodo']
	print(periodo)
	asignatura= request.POST['asignatura']
	print(asignatura)
	actividad1 = request.POST['actividad1']
	print(actividad1)
	actividad2 = request.POST['actividad2']
	print(actividad2)
	actividad3 = request.POST['actividad3']
	print(actividad3)
	#obtener instancias de objetos
	al = Alumno.objects.get(nie=nie)
	es = Especialidad.objects.get(codigo_especialidad=especialidad)
	sec = Seccion.objects.get(id_seccion = seccion)
	ni = Nivel.objects.get(id_nivel=nivel)
	pe = Periodo.objects.get(id_periodo= periodo)
	asi = Asignatura.objects.get(codigo_asignatura = asignatura)

	#Intancia de cada objeto de actividad
	act1 = Actividad.objects.get(id_actividad=1)
	act2 = Actividad.objects.get(id_actividad=2)
	act3 = Actividad.objects.get(id_actividad=3)

	#Creacion de los registros del alumno
	notaactividad1 = NotasActividad(id_especialidad=es, id_nivel = ni, id_seccion =sec, id_alumno = al, id_periodo = pe, id_asignatura = asi, id_actividad =act1, valor = actividad1 )
	notaactividad1.save()
	notaactividad2 = NotasActividad(id_especialidad=es, id_nivel = ni, id_seccion =sec, id_alumno = al, id_periodo = pe, id_asignatura = asi, id_actividad =act2, valor = actividad2 )
	notaactividad2.save()
	notaactividad3 = NotasActividad(id_especialidad=es, id_nivel = ni, id_seccion =sec, id_alumno = al, id_periodo = pe, id_asignatura = asi, id_actividad =act3, valor = actividad3 )
	notaactividad3.save()
	
	return render(
		request,
		'app1/registro_notas.html'
		)

#Funcion para filtrar en los listbox la informacion 
def registronota(request):
	dic = consultalistas()
	periodo = Periodo.objects.all()
	materia = Asignatura.objects.all()
	context={'periodo':periodo, 'materia':materia}
	dic.update(context)
	return render(
		request,
		'app1/registro_notas.html',
		dic,
		)

#Funcion para recuperar a los alumnos de dicha especialidad
def registroconsulta(request):
	if request.method =='POST':
		especialidad = request.POST['especialidad']
		seccion = request.POST['seccion']
		nivel = request.POST['nivel']
		periodo = request.POST['periodo']
		asignatura = request.POST['asignatura']

		matricula = Matricula.objects.filter(especialidad_matricula = especialidad).filter(nivel_matricula = nivel).filter(seccion_matricula=seccion)

		nota1 = NotasActividad.objects.filter(id_especialidad = especialidad).filter(id_nivel=nivel).filter(id_actividad = 1).filter(id_seccion = seccion).filter(id_asignatura=asignatura).filter(id_periodo=periodo)
		nota2 = NotasActividad.objects.filter(id_especialidad = especialidad).filter(id_nivel=nivel).filter(id_actividad = 2).filter(id_seccion = seccion).filter(id_asignatura=asignatura).filter(id_periodo=periodo)
		nota3 = NotasActividad.objects.filter(id_especialidad = especialidad).filter(id_nivel=nivel).filter(id_actividad = 3).filter(id_seccion = seccion).filter(id_asignatura=asignatura).filter(id_periodo=periodo)
		promedio=[]
		i=0
		while(i < len(nota1)):
			promedio.append("{0:.2f}".format((nota1[i].valor*0.35)+(nota2[i].valor*0.35)+(nota3[i].valor*0.30)))
			i+=1

		print(promedio)

		context={'matricula': matricula, 'nota3':nota3, 'nota2': nota2, 'nota1':nota1, 'promedio':promedio}
		return render(request, 'app1/registro_notas.html', context)

#Metodo para la vista de consultar notas
def ConsultaNotas(request):
	context = consultalistas()
	periodo = Periodo.objects.all()
	dic = {'periodo': periodo}
	context.update(dic)
	return render(
		request,
		'app1/consultar_notas.html',
		context,
		)
def NotasMostrar(request):
	if request.method == 'POST':
		especialidad = request.POST['especialidad']
		seccion = request.POST['seccion']
		nivel = request.POST['nivel']
		periodo = request.POST['periodo']
		matricula = Matricula.objects.filter(especialidad_matricula = especialidad, nivel_matricula = nivel, seccion_matricula = seccion).order_by('alumno__apellidos_alumno').desc()
		notas =NotasActividad.objects.filter(id_especialidad = especialidad, id_seccion = seccion, id_nivel = nivel, id_periodo = periodo)
		asignatura = Especialidad_Asignatura.objects.filter(especialidad=especialidad, nivel = nivel)
		context ={'notas': notas, 'matricula': matricula, 'asignatura': asignatura}

		return render(
			request,
			'app1/consultar_notas.html',
			context,
		)
#Clase que crear una nueva asignatura
class crearAsignatura(CreateView):
	template_name='app1/crear_asignatura.html'
	form_class = AsignaturaForm
	success_url= reverse_lazy('gestor:index')

class editarAsignatura(UpdateView):
	model = Asignatura
	template_name='app1/crear_asignatura.html'
	form_class=AsignaturaForm
	success_url=reverse_lazy('gestor:gestion_asignatura')

class listadoAsignatura(ListView):
	model = Asignatura
	template_name='app1/gestion_asignatura.html'
	context_object_name ='asignatura'

class eliminarAsignatura(DeleteView):
	model = Asignatura
	template_name = 'app1/eliminar_asignatura.html'
	success_url=reverse_lazy('gestor:gestion_asignatura')

class modificarNotas(UpdateView):
	model = NotasActividad
	template_name = 'app1/modificar_notas.html'
	form_class = NotasActividadForm
	success_url= reverse_lazy('gestor:registro_consulta')


class editarAlumno(UpdateView):
	model = Matricula
	template_name = 'app1/editar_alumno.html'
	form_class = MatriculaForm
	success_url = reverse_lazy('gestor:consulta_alumno')