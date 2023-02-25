from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Appsma.models import Avatar

# Create your forms here.
class ClientesFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    telefono = forms.IntegerField()


class AlojamientosFormulario(forms.Form):

    nombreA = forms.CharField(max_length=20)
    capacidad = forms.IntegerField()
    habitaciones = forms.IntegerField()
    precioxdia = forms.FloatField()


class VehiculosFormulario(forms.Form):

    nombreV = forms.CharField(max_length=40)
    asientos = forms.IntegerField()
    preciodiario = forms.FloatField()


class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "repetir contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]



class formularioEditar(UserCreationForm):
    

    email = forms.EmailField()
    password1 = forms.CharField(label = "contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "repetir contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]


class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ["usuario", "imagen"]

    