from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('lista_profesionales/', views.profesionalListView.as_view(template_name='profesional_list.html'), name='lista_profesionales'),
    path('crear_profesional/', views.profesionalCreateView.as_view(template_name='profesional_form.html'), name='crear_profesional'),
    path('detalle_profesional/<int:pk>/', views.profesionalDetailView.as_view(template_name='profesional_detail.html'), name='detalle_profesional'),
    path('borrar_profesional/<int:pk>/', views.profesionalDeleteView.as_view(template_name='profesional_confirm_delete.html'), name='borrar_profesional'),
    path('lista_pacientes/', views.pacienteListView.as_view(template_name='paciente_list.html'), name='lista_pacientes'),
    path('crear_paciente/', views.pacienteCreateView.as_view(template_name='paciente_form.html'), name='crear_paciente'),
    path('detalle_paciente/<int:pk>/', views.pacienteDetailView.as_view(template_name='paciente_detail.html'), name='detalle_paciente'),
    path('borrar_paciente/<int:pk>/', views.pacienteDeleteView.as_view(template_name='paciente_confirm_delete.html'), name='borrar_paciente'),
    path('lista_consultas/', views.consultaListView.as_view(template_name='consulta_list.html'), name='lista_consultas'),
    path('crear_consulta/', views.ConsultaCreateView.as_view(template_name='consulta_form.html'), name='crear_consulta'),
    path('detalle_consulta/<int:pk>/', views.ConsultaDetailView.as_view(template_name='consulta_detail.html'), name='detalle_consulta'),
    path('borrar_consulta/<int:pk>/', views.ConsultaDeleteView.as_view(template_name='consulta_confirm_delete.html'), name='borrar_consulta'),
   
]

