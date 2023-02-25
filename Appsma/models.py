from django.db import models
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User


# Create your models here.
class Clientes(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombre}  --------  Apellido: {self.apellido} ------------- Email: {self.email} ----------- Telefono: {self.telefono}"

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField(blank=True)





class Alojamientos(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombreA}  --------  Capacidad: {self.capacidad} ------------- Habitaciones: {self.habitaciones}  --------------- Preciodiario: {self.precioxdia}"

    nombreA = models.CharField(max_length=20)
    capacidad = models.IntegerField()
    habitaciones = models.IntegerField()
    precioxdia = models.FloatField()


class Vehiculos(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombreV}  --------  Asientos: {self.asientos} ------------- Preciodiario: {self.preciodiario}"

    nombreV = models.CharField(max_length=40)
    asientos = models.IntegerField()
    preciodiario = models.FloatField()


#class VehiculoList(ListView):
#
 #   model = Vehiculos
  #  template_name = "vervehiculos.html"


#class VehiculoDetalle(DetailView):

 #   model = Vehiculos
  #  template_name = "vehiculodetalle.html"

#class VehiculoCreacion(CreateView):

 #   model = Vehiculos
  #  success_url = "/vervehiculos/list"
   # fields = ['nombreV','asientos']


#class VehiculoUpdate(UpdateView):

 #   model = Vehiculos
  #  success_url = "/vervehiculos/list"
   # fields = ['nombreV','asientos']


#class VehiculoDelete(DeleteView):

 #   model = Vehiculos
  #  success_url = "/vervehiculos/list"
   # fields = ['nombreV','asientos']



#class AlojamientosLista(ListView):

 #   model = Alojamientos
  #  template_name = "alojamientos_list.html"
#

#class AlojamientoDetalle(DetailView):

 #   model = Alojamientos
  #  template_name = "alojamientodetalle.html"

#class AlojamientoCreacion(CreateView):

 #   model = Alojamientos
  #  success_url = "/veralojamientos/list"
   # fields = ['nombreA','capacidad']


#class AlojamientoUpdate(UpdateView):
#
 #   model = Alojamientos
  #  success_url = "/veralojamientos/list"
   # fields = ['nombreA','capacidad','precioxdia']


#class AlojamientoDelete(DeleteView):

 #   model = Alojamientos
  #  success_url = "/veralojamientos/list"
   # fields = ['nombreA','asientos']


class Avatar(models.Model):
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', null=True, blank=True, default=None)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"

    def first(self, request):

       return self.filter(usuario=request.user)
    
