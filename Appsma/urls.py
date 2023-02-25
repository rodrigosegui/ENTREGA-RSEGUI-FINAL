from django.urls import path
from Appsma.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('alojamientos/list/', AlojamientosLista.as_view(), name="Alojamientos" ),
    path('alojamientos/<int:pk>/', AlojamientoDetalle.as_view(), name="Alojamientoelegido" ),
    #path('alojamientos/borrar/<int:pk>', AlojamientoDelete.as_view(), name="eliminaralojamiento"),
    #path('alojamientos/editar/<int:pk>', AlojamientoUpdate.as_view(), name="editaralojamiento"),
    #path('alojamientos/crear/', AlojamientoCreate.as_view(), name="Nueva Casa"),
    path('editaralojamiento/<alojamiento_elegido>/', editar_alojamiento, name="editaralojamiento"),
    path('eliminaralojamiento/<alojamiento_elegido>/', eliminar_alojamiento, name="eliminaralojamiento"),
    path('buscaralojamiento/', buscaralojamiento, name = "Busca tu alojamiento"),
    path('resultadosalojamiento/', resultadosalojamiento, name="Resultados Alojamientos"),
    path('agregaralojamiento/', agregaralojamiento, name="Nuevos"),
    path('agregarImagen/', agregarImagen, name="subir avatar"),
    

    #path('vervehiculos/', ver_vehiculos, name="Vehiculos"),
    path('vehiculos/vehiculos_list/', VehiculoLista.as_view(), name="Vehiculos"),
    path('vehiculos/<int:pk>/', VehiculoDetalle.as_view(), name="Vehiculoelegido" ),
    path('buscaravehiculo/', buscarvehiculo, name = "Busca tu Vehiculo"),
    path('resultadosvehiculo/', resultadosvehiculo, name="Resultados Vehiculos"),
    path('agregarvehiculo/', agregarvehiculo, name="Nuevos Vehiculos"),
    path('editarvehiculo/<vehiculo_elegido>/', editar_vehiculo, name="editarvehiculo"),
    path('eliminarvehiculo/<vehiculo_elegido>/', eliminar_vehiculo, name="eliminarvehiculo"),

    #path('vercliente/', ver_clientes, name="Clientes"), 
    path('clientes/clientes_list/', ClienteLista.as_view(), name="Clientes"),
    path('clientes/<int:pk>/', ClienteDetalle.as_view(), name="Clienteelegido" ),
    path('buscarcliente/', buscarcliente, name = "Buscar Clientes"),
    path('resultadoscliente/', resultadoscliente, name="Resultados Clientes"),
    path('agregarcliente/', agregarcliente, name = "Nuevos Clientes"),
    path('editarcliente/<cliente_elegido>/', editar_cliente, name = "editarcliente"),
    path('eliminarcliente/<cliente_elegido>/', eliminar_cliente, name="eliminarcliente"),
       
    
    
    
    path('inicio/', inicio, name="Inicio"),
    path('nosotros/', nosotros, name="Nosotros"),
    path('iniciar/', iniciar, name="Login"),
    path('registro/', registro, name="Registrarse"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editar/', editar_usuario, name="EditarUsuario"),
    
    
]