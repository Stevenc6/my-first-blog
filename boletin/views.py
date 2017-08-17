from django.shortcuts import render

#importando form
from .forms import RegForm, RegModelForm
from .models import Registrado
# Create your views here.

def inicio(request):
	titulo = "HOLA"
	#valida al usuario cuando se loguea.
	if request.user.is_authenticated():
		titulo = "Bienvenido %s" %(request.user)

	form = RegModelForm(request.POST or None)

	context = {
		"titulo" : titulo,
		"el_form": form,
	}


	#print(dir(form))
	if form.is_valid():
		instance = form.save(commit=False)
		#Se escribe commit = false para que despues de eso se pueda verificar la info y agregar otras cosas
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		if not instance.nombre:
			instance.nombre = "PERSONA"
		instance.save()



		context = {
			"titulo": "Gracias %s!" %(nombre)

		}

		if not nombre:
			context = {
				"titulo": "Gracias persona!"
			}

		print(instance)
		print(instance.timestamp)
		#print(form.cleaned_data)
		#cuando se llena el formulario y se recupera el nombre
		#form_data = form.cleaned_data
		#print(form_data.get("nombre"))		
		#abc = form_data.get("email")
		#abc2 = form_data.get("nombre")	
		#obj = Registrado.objects.create(email=abc, nombre=abc2)	

		#obj = Registrado()
		#obj.email = abc
		#obj.save()

	return render(request,"inicio.html",context)