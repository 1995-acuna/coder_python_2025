from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear_profesional/', views.crear_profesional, name='crear_profesional'),
    path('crear_paciente/', views.crear_paciente, name='crear_paciente'),
    path('crear_consulta/', views.crear_consulta, name='crear_consulta'),
]

