from django import forms

class CursoFormulario(forms.Form):
    nombre=forms.CharField()
    camada=forms.IntegerField()
    
class ProfeFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()
    profesion=forms.CharField()
    
class AlumnoFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()
    
class EntregableFormulario(forms.Form):
    nombre=forms.CharField()
    fecha_entrega=forms.DateField()
    entregado=forms.BooleanField()