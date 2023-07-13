from django.shortcuts import render
from CoderApp.models import Curso,Profesor,Estudiantes,Entregables
from CoderApp.forms import CursoFormulario, ProfeFormulario,AlumnoFormulario,EntregableFormulario
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

#def cursos(request):
    #return render(request,'cursos.html')

def estudiantes(request):
    return render(request,'estudiantes.html')

def profesores(request):
    return render(request,'profesores.html')

def entregables(request):
    return render(request,'entregables.html')

def cursos(request):
    if request.method == 'POST':
        myForm=CursoFormulario(request.POST) #Aqui llega la info del html
        print(myForm)
        if myForm.is_valid:
            info=myForm.cleaned_data
            curso=Curso(nombre=info['nombre'], camada=info['camada'])
            curso.save()
            return render(request,'cursos.html')
    else:
        myForm=CursoFormulario()
    return render(request,'cursos.html',{'myForm':myForm})

def profesores(request):
    if request.method == 'POST':
        myForm=ProfeFormulario(request.POST)
        print(myForm)
        if myForm.is_valid:
            info=myForm.cleaned_data
            profesor=Profesor(nombre=info['nombre'],apellido=info['apellido'],email=info['email'],profesion=info['profesion'])
            profesor.save()
            return render(request,'profesores.html')
    else:
        myForm=ProfeFormulario()
    return render(request,'profesores.html',{'myForm':myForm})
        
def estudiantes(request):
    if request.method == 'POST':
        myForm=AlumnoFormulario(request.POST)  
        print(myForm)
        if myForm.is_valid:
            info=myForm.cleaned_data
            alumno=Estudiantes(nombre=info['nombre'],apellido=info['apellido'],email=info['email'])
            alumno.save()
            return render(request,'estudiantes.html')    
    else:
        myForm=AlumnoFormulario()
    return render(request,'estudiantes.html',{'myForm':myForm})

def entregables(request):
    if request.method=='POST':
        myForm=EntregableFormulario(request.POST)
        print(myForm)
        if myForm.is_valid:
            info=myForm.cleaned_data
            entreg=Entregables(nombre=info['nombre'],fecha_entrega=info['fecha_entrega'],entregado=info['entregado'])
            entreg.save()
            return render(request,'entregables.html')
    else:
        myForm=EntregableFormulario()
    return render(request,'entregables.html',{'myForm':myForm})
        
        
def busquedacamada(request):
    return render(request,'busquedacamada.html')

def buscar(request):
    if request.GET['camada']:
        camada=request.GET['camada']
        curso=Curso.objects.filter(camada__icontains=camada)
        return render(request, 'inicio.html', {'nombre':curso,'camada':camada})
    else:
        respuesta='No hay datos que buscar'
        return render (request, "inicio.html", {'respuesta': respuesta})