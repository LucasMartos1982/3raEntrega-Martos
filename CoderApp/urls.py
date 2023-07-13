from django.urls import path
from CoderApp import views


urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('cursos/',views.cursos, name='cursos'),
    path('estudiantes/',views.estudiantes, name='estudiantes'),
    path('profesores/',views.profesores, name='profesores'),
    path('entregables/',views.entregables, name='entregables'),
    #path('cursoformulario/',views.cursoformulario,name='cursoformulario'),
    #path('profeformulario/',views.profeformulario,name='profeformulario'),
    #path('alumnoformulario/',views.estudianteformulario,name='alumnoformulario'),
    #path('entregableformulario/',views.entregableformulario,name='entregableformulario'),
    path('busquedacamada/',views.busquedacamada, name='busquedacamada'),
    path('buscar/',views.buscar),
]