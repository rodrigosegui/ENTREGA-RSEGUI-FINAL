from django.shortcuts import render
from Appsma.models import *
from Appsma.forms import *
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(request):

    return render(request,"inicio.html")

#vista para crear avatares
@login_required
def agregarImagen(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        

        if miFormulario.is_valid():
            usuarioActual = User.objects.get(username=request.user)
            avatar = Avatar(usuario=usuarioActual, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, "inicio.html")
        
    else:
        miFormulario = AvatarFormulario()

    return render(request, "agregarimg.html", {"form": miFormulario})


def nosotros(request):

    return render(request,"nosotros.html")

def ver_alojamientos(request):

    alojamientos = Alojamientos.objects.all() #sacando todas los alojamientos de la base de datos

    return render(request,"veralojamientos.html", {"alojamientos_all":alojamientos})

@login_required
def ver_clientes(request):

    clientes = Clientes.objects.all() #sacando todas los alojamientos de la base de datos

    return render(request,"verclientes.html", {"clientes_all":clientes})

def ver_vehiculos(request):
    
    vehiculos = Vehiculos.objects.all() #sacando todas los alojamientos de la base de datos

    return render(request,"vervehiculos.html", {"vehiculos_all":vehiculos})



@login_required
def agregaralojamiento(request):

    if request.method == 'POST':
        miFormulario = AlojamientosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            alojamientos = Alojamientos(nombreA=informacion["nombreA"],habitaciones=informacion["habitaciones"], capacidad=informacion["capacidad"],precioxdia=informacion["precioxdia"])
            alojamientos.save()
            return render(request, "inicio.html")
        
    else:
        miFormulario = AlojamientosFormulario()

    return render(request, "agregaralojamiento.html", {"miFormulario": miFormulario})
@login_required
def agregarvehiculo(request):

    if request.method == 'POST':
        miFormulario = VehiculosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            vehiculos = Vehiculos(nombreV=informacion["nombreV"],asientos=informacion["asientos"], preciodiario=informacion["preciodiario"])
            vehiculos.save()
            return render(request, "vehiculos_list.html")
        
    else:
        miFormulario = VehiculosFormulario()

    return render(request, "agregarvehiculo.html", {"miFormulario": miFormulario})
@login_required
def agregarcliente(request):

    if request.method == 'POST':
        miFormulario = ClientesFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            clientes = Clientes(nombre=informacion["nombre"],apellido=informacion["apellido"], telefono=informacion["telefono"],email=informacion["email"])
            clientes.save()
            return render(request, "inicio.html")
        
    else:
        miFormulario = ClientesFormulario()

    return render(request, "agregarcliente.html", {"miFormulario": miFormulario})

@login_required
def editar_alojamiento(request, alojamiento_elegido):
    alojamiento = Alojamientos.objects.get(nombreA=alojamiento_elegido)

    if request.method =='POST':

        miFormulario = AlojamientosFormulario(request.POST)

        if miFormulario.is_valid():

            infoDict = miFormulario.cleaned_data

            alojamiento.nombreA = infoDict["nombreA"]
            alojamiento.capacidad = infoDict["capacidad"]
            alojamiento.habitaciones = infoDict["habitaciones"]
            alojamiento.precioxdia = infoDict["precioxdia"]

            alojamiento.save()
            return render(request, "inicio.html")
        
    else:
        miFormulario = AlojamientosFormulario(initial={"nombreaA":alojamiento.nombreA,"capacidad":alojamiento.capacidad,"habitaciones":alojamiento.habitaciones,"precioxdia":alojamiento.precioxdia})

    return render(request,"editar_alojamiento.html", {"miFormulario":miFormulario, "nombreA":alojamiento_elegido.nombreA} )
@login_required
def editar_vehiculo(request, vehiculo_elegido):
    vehiculo_elegido = Vehiculos.objects.get(nombreV=vehiculo_elegido)

    if request.method =='POST':

        miFormulario = VehiculosFormulario(request.POST)

        if miFormulario.is_valid():

            infoDict = miFormulario.cleaned_data

            vehiculo_elegido.nombreV = infoDict["nombreV"]
            vehiculo_elegido.asientos = infoDict["asientos"]
            vehiculo_elegido.preciodiario = infoDict["preciodiario"]

            vehiculo_elegido.save()
            return render(request, "inicio.html")
        
    else:
        miFormulario = AlojamientosFormulario()

    return render(request,"editar_alojamiento.html", {"formulario1":miFormulario} )

@login_required
def editar_cliente(request, cliente_elegido):
    cliente_elegido = Clientes.objects.get(nombre=cliente_elegido)

    if request.method =='POST':

        miFormulario = ClientesFormulario(request.POST)

        if miFormulario.is_valid():

            infoDict = miFormulario.cleaned_data

            cliente_elegido.nombre = infoDict["nombre"]
            cliente_elegido.apellido = infoDict["apellido"]
            cliente_elegido.telefono = infoDict["telefono"]
            cliente_elegido.email = infoDict["mail"]

            cliente_elegido.save()
            return render(request, "inicio.html")
        
    else:
        miFormulario = ClientesFormulario()

    return render(request,"editar_cliente.html", {"formulario1":miFormulario} )





def buscaralojamiento(request):
    return render(request, "buscaralojamiento.html")

def resultadosalojamiento(request):

    capacidadbusqueda = request.GET["capacidad"]
    resultadoscapacidad = Alojamientos.objects.filter(capacidad__exact=capacidadbusqueda)
    return render(request, "resultadosalojamiento.html" , {"info1":capacidadbusqueda, "info2":resultadoscapacidad})




def buscarvehiculo(request):
    return render(request, "buscarvehiculo.html")

def resultadosvehiculo(request):

    asientosbusqueda = request.GET["asientos"]
    resultadoscapacidad = Vehiculos.objects.filter(asientos__icontains=asientosbusqueda)
    return render(request, "resultadosvehiculo.html" , {"info1":asientosbusqueda, "info2":resultadoscapacidad})




def buscarcliente(request):
    return render(request, "buscarcliente.html")

def resultadoscliente(request):

    clientesbusqueda = request.GET["nombre"]
    resultadosnombre = Clientes.objects.filter(nombre__icontains=clientesbusqueda)
    return render(request, "resultadoscliente.html" , {"info1":clientesbusqueda, "info2":resultadosnombre})

@login_required
def eliminar_alojamiento(request, alojamiento_elegido):
    
    alojamiento = Alojamientos.objects.get(nombreA=alojamiento_elegido)
    alojamiento.delete()

    alojamientos = Alojamientos.objects.all()
    context = {"alojamientos_all":alojamientos}

    return render(request,"alojamientos_list.html", context)
@login_required
def editar_alojamiento(request, alojamiento_elegido):
    
    alojamiento = Alojamientos.objects.get(nombreA=alojamiento_elegido)

    if request.method =='POST':

        miFormulario = AlojamientosFormulario(request.POST)

        if miFormulario.is_valid():

            infoDict = miFormulario.cleaned_data

            alojamiento.nombreA = infoDict["nombreA"]
            alojamiento.capacidad = infoDict["capacidad"]
            alojamiento.habitaciones = infoDict["habitaciones"]
            alojamiento.precioxdia = infoDict["precioxdia"]

            alojamiento.save()
            return render(request, "alojamientos_list.html")
        
    else:
        miFormulario = AlojamientosFormulario(initial={"nombreA":alojamiento.nombreA,"capacidad":alojamiento.capacidad,"habitaciones":alojamiento.habitaciones,"precioxdia":alojamiento.precioxdia})

    return render(request,"editar_alojamiento.html", {"miFormulario":miFormulario, "nombreA":alojamiento_elegido} )

@login_required
def eliminar_vehiculo(request, vehiculo_elegido):
    
    vehiculo = Vehiculos.objects.get(nombreV=vehiculo_elegido)
    vehiculo.delete()

    vehiculos = Vehiculos.objects.all()
    context = {"vehiculos_all":vehiculos}

    return render(request,"vehiculos_list.html", context)

@login_required
def editar_vehiculo(request, vehiculo_elegido):
    
    vehiculo = Vehiculos.objects.get(nombreV=vehiculo_elegido)

    if request.method =='POST':

        miFormulario = VehiculosFormulario(request.POST)

        if miFormulario.is_valid():

            infoDict = miFormulario.cleaned_data

            vehiculo.nombreV = infoDict["nombreV"]
            vehiculo.asientos = infoDict["asientos"]
            vehiculo.preciodiario = infoDict["preciodiario"]

            vehiculo.save()
            return render(request, "vehiculos_list.html")
        
    else:
        miFormulario = VehiculosFormulario(initial={"nombreV":vehiculo.nombreV,"asientos":vehiculo.asientos,"preciodiario": vehiculo.preciodiario})

    return render(request,"editar_vehiculo.html", {"miFormulario":miFormulario, "nombreV":vehiculo_elegido} )

@login_required
def eliminar_cliente(request, cliente_elegido):
    
    cliente = Clientes.objects.get(nombre=cliente_elegido)
    cliente.delete()

    clientes = Clientes.objects.all()
    context = {"clientes_all":clientes}

    return render(request,"verclientes.html", context)


@login_required
def editar_cliente(request, cliente_elegido):
    
    cliente = Clientes.objects.get(nombre=cliente_elegido)

    if request.method =='POST':

        miFormulario = ClientesFormulario(request.POST)

        if miFormulario.is_valid():

            infoDict = miFormulario.cleaned_data

            cliente.nombre = infoDict["nombre"]
            cliente.apellido = infoDict["apellido"]
            cliente.email = infoDict["email"]
            cliente.telefono = infoDict["telefono"]

            cliente.save()
            return render(request, "verclientes.html")
        
    else:
        miFormulario = ClientesFormulario(initial={"nombre":cliente.nombre,"apellido":cliente.apellido,"email":cliente.email,"telefono":cliente.telefono})

    return render(request,"editar_cliente.html", {"miFormulario":miFormulario, "nombre":cliente_elegido} )


def iniciar(request):
    if request.method == "POST":

        form =AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user= authenticate(username = usuario, password = contra)

            if user:

                login(request, user)

                return render(request, "inicio.html", {"mensaje":f"Bienvenido {user}"})

            else:

                return render(request, "inicio.html", {"mensaje":"Datos incorrectos."})   

        else:

                return render(request, "inicio.html", {"mensaje":"formulario errone."}) 
    form = AuthenticationForm()

    return render(request, "iniciar.html", {"formulario":form}) 


def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()

            return render(request, "inicio.html", {"mensaje":"usuario creado"})
        
    else:

        form = UsuarioRegistro()

    return render(request, "registro.html", {"formulario":form})


def editar_usuario(request):

    usuario = request.user

    if request.method == "POST":

        form = formularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.set_password(info["password2"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "inicio.html")
        
    else:

        form = formularioEditar(initial={
            "email":usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name,  


            })

    return render(request, "editarPerfil.html", {"formulario": form, "usuario":usuario})

class VehiculoLista(ListView):

    model = Vehiculos
    template_name = "vehiculos_list.html"


class VehiculoDetalle(DetailView):

    model = Vehiculos
    template_name = "vehiculodetalle.html"

class VehiculoCreacion(CreateView):

    model = Vehiculos
    success_url = "/vervehiculos/list"
    fields = ['nombreV','asientos']


class VehiculoUpdate(UpdateView):

    model = Vehiculos
    success_url = "/vervehiculos/list"
    fields = ['nombreV','asientos']


class VehiculoDelete(DeleteView):

    model = Vehiculos
    success_url = "/vervehiculos/list"
    fields = ['nombreV','asientos']



class AlojamientosLista(ListView):

    model = Alojamientos
    template_name = "alojamientos_list.html"


class AlojamientoDetalle(DetailView):

    model = Alojamientos
    template_name = "alojamientodetalle.html"

class AlojamientoCreate(CreateView):

    model = Alojamientos
    success_url = "/alojamientos/list"
    fields = ['nombreA','capacidad','habitaciones', 'precioxdia']


class AlojamientoUpdate(UpdateView):

    model = Alojamientos
    success_url = "/alojamientos/list"
    fields = ['nombreA','capacidad','habitaciones', 'precioxdia']


class AlojamientoDelete(DeleteView):

    model = Alojamientos
    success_url = "/alojamientos/list"
    fields = ['nombreA','capacidad','habitaciones', 'precioxdia']


class ClienteLista(ListView):

    model = Clientes
    template_name = "clientes_list.html"


class ClienteDetalle(DetailView):

    model = Clientes
    template_name = "clientedetalle.html"

class ClienteCreacion(CreateView):

    model = Clientes
    success_url = "/clientes/list"
    fields = ['nombre','apellido','email','telefono']


class ClienteUpdate(UpdateView):

    model = Clientes
    success_url = "/clientes/list"
    fields = ['nombre','apellido','email','telefono']


class ClienteDelete(DeleteView):

    model = Clientes
    success_url = "/clientes/list"
    fields = ['nombre','apellido','email','telefono']


#ver final resumen clase23 y video anterior de vistas de clase lista

#def __str__(self):
#    return f"nombreV: {self.nombreV} - asientos {self.asientos}"