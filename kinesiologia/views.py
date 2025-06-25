from django.shortcuts import render, redirect #redirect
# from .forms import ProfesionalForm, PacienteForm, ConsultaForm
from django.contrib import messages
from .models import Profesional, Paciente, Consulta
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def home(request):
    return render(request, 'base.html')
###################################################################################################################
# def crear_profesional(request):
#     form = ProfesionalForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         messages.success(request, "Profesional guardado exitosamente.")
#         return redirect('home')
#     return render(request, 'crear_profesional.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class profesionalListView(ListView):
    model = Profesional
    template_name = 'profesional_list.html'
    context_object_name = 'profesionales'

@method_decorator(login_required, name='dispatch')
class profesionalCreateView(CreateView):
    model = Profesional
    template_name = 'profesional_form.html'
    fields = '__all__'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Profesional guardado exitosamente.")
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class profesionalDetailView(DetailView):
    model = Profesional
    template_name = 'profesional_detail.html'
    context_object_name = 'profesional'

@method_decorator(login_required, name='dispatch')
class profesionalDeleteView(DeleteView):
    model = Profesional
    template_name = 'profesional_confirm_delete.html'
    success_url = reverse_lazy("home")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Profesional eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
##################################################################################################################3
# def crear_paciente(request):
#     form = PacienteForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         messages.success(request, "Paciente guardado exitosamente.")
#         return redirect('home')
#     return render(request, 'crear_paciente.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class pacienteListView(ListView):
    model = Paciente
    template_name = 'paciente_list.html'
    context_object_name = 'pacientes'

@method_decorator(login_required, name='dispatch')
class pacienteCreateView(CreateView):
    model = Paciente
    template_name = 'paciente_form.html'
    fields = '__all__'
    success_url = reverse_lazy("lista_pacientes")

    def form_valid(self, form):
        messages.success(self.request, "Paciente guardado exitosamente.")
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class pacienteDetailView(DetailView):
    model = Paciente
    template_name = 'paciente_detail.html'
    context_object_name = 'paciente'
    
@method_decorator(login_required, name='dispatch')
class pacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'paciente_confirm_delete.html'
    success_url = reverse_lazy("lista_pacientes")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Paciente eliminado correctamente.")
        return super().delete(request, *args, **kwargs)

###############################################################################################
# def crear_consulta(request):
#     form = ConsultaForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('home')
#     return render(request, 'crear_consulta.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class consultaListView(ListView):
    model = Consulta
    template_name = 'consulta_list.html'
    context_object_name = 'consultas'

@method_decorator(login_required, name='dispatch')
class ConsultaCreateView(CreateView):
    model = Consulta
    template_name = 'consulta_form.html'
    fields = '__all__'
    success_url = reverse_lazy("lista_consultas")

    def form_valid(self, form):
        messages.success(self.request, "Consulta guardada exitosamente.")
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class ConsultaDetailView(DetailView):
    model = Consulta
    template_name = 'consulta_detail.html'
    context_object_name = 'consulta'

@method_decorator(login_required, name='dispatch')
class ConsultaDeleteView(DeleteView):
    model = Consulta
    template_name = 'consulta_confirm_delete.html'
    success_url = reverse_lazy("lista_consultas")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Consulta eliminada correctamente.")
        return super().delete(request, *args, **kwargs)

################################################################################################

@login_required
def listar_registros(request):
    profesionales = Profesional.objects.all()
    pacientes = Paciente.objects.all()
    consultas = Consulta.objects.all()
    return render(request, 'listar_registros.html', {'profesionales': profesionales, 'pacientes': pacientes, 'consultas': consultas})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Usuario registrado y logueado correctamente.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})




