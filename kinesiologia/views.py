from django.shortcuts import render, get_object_or_404, redirect #redirect
# from .forms import ProfesionalForm, PacienteForm, ConsultaForm,ExamenFisicoForm
from django.contrib import messages
from .models import Profesional, Paciente, Consulta, ExamenFisico, Sesion
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import ExamenFisicoForm, SesionForm
from django.contrib.auth.decorators import login_required
from .superuser_access import superuser_required, SuperuserRequiredMixin




@superuser_required
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


class profesionalListView(SuperuserRequiredMixin, ListView):
    model = Profesional
    template_name = 'profesional_list.html'
    context_object_name = 'profesionales'


class profesionalCreateView(SuperuserRequiredMixin, CreateView):
    model = Profesional
    template_name = 'profesional_form.html'
    fields = '__all__'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Profesional guardado exitosamente.")
        return super().form_valid(form)
    

class profesionalDetailView(SuperuserRequiredMixin, DetailView):
    model = Profesional
    template_name = 'profesional_detail.html'
    context_object_name = 'profesional'


class profesionalDeleteView(SuperuserRequiredMixin, DeleteView):
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


class pacienteListView(SuperuserRequiredMixin, ListView):
    model = Paciente
    template_name = 'paciente_list.html'
    context_object_name = 'pacientes'


class pacienteCreateView(SuperuserRequiredMixin, CreateView):
    model = Paciente
    template_name = 'paciente_form.html'
    fields = '__all__'
    success_url = reverse_lazy("lista_pacientes")

    def form_valid(self, form):
        messages.success(self.request, "Paciente guardado exitosamente.")
        return super().form_valid(form)
    

class pacienteDetailView(SuperuserRequiredMixin, DetailView):
    model = Paciente
    template_name = 'paciente_detail.html'
    context_object_name = 'paciente'
    

class pacienteDeleteView(SuperuserRequiredMixin, DeleteView):
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



class consultaListView(SuperuserRequiredMixin, ListView):
    model = Consulta
    template_name = 'consulta_list.html'
    context_object_name = 'consultas'


class ConsultaCreateView(SuperuserRequiredMixin, CreateView):
    model = Consulta
    template_name = 'consulta_form.html'
    fields = '__all__'
    success_url = reverse_lazy("lista_consultas")

    def form_valid(self, form):
        messages.success(self.request, "Consulta guardada exitosamente.")
        return super().form_valid(form)
    

class ConsultaDetailView(SuperuserRequiredMixin, DetailView):
    model = Consulta
    template_name = 'consulta_detail.html'
    context_object_name = 'consulta'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['examen'] = self.object.examen_fisico
        except ExamenFisico.DoesNotExist:
            context['examen'] = None
        # Agregar sesiones del paciente   
    
        context['sesiones_paciente'] = Sesion.objects.filter(paciente=self.object.Paciente).order_by('-fecha')
        return context


class ConsultaDeleteView(SuperuserRequiredMixin, DeleteView):
    model = Consulta
    template_name = 'consulta_confirm_delete.html'
    success_url = reverse_lazy("lista_consultas")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Consulta eliminada correctamente.")
        return super().delete(request, *args, **kwargs)

################################################################################################


@superuser_required
def listar_registros(request):
    profesionales = Profesional.objects.all()
    pacientes = Paciente.objects.all()
    consultas = Consulta.objects.all()
    return render(request, 'listar_registros.html', {'profesionales': profesionales, 'pacientes': pacientes, 'consultas': consultas})


@superuser_required
def crear_examen_fisico(request, consulta_id):
    consulta = get_object_or_404(Consulta, pk=consulta_id)
    if hasattr(consulta, 'examen_fisico'):
        return redirect('detalle_consulta', pk=consulta_id)
    if request.method == 'POST':
        form = ExamenFisicoForm(request.POST)
        if form.is_valid():
            examen = form.save(commit=False)
            examen.consulta = consulta
            examen.save()
            return redirect('detalle_consulta', pk=consulta_id)
    else:
        form = ExamenFisicoForm()
    return render(request, 'examen_fisico_form.html', {'form': form, 'consulta': consulta})


class EditarExamenFisicoView(SuperuserRequiredMixin, UpdateView):
    model = ExamenFisico
    form_class = ExamenFisicoForm
    template_name = 'examen_fisico_form.html'

    def form_valid(self, form):
        messages.success(self.request, "Examen físico editado exitosamente.")
        return super().form_valid(form)

    def get_success_url(self):
        return f"/detalle_consulta/{self.object.consulta.id}/"

@superuser_required
def sesion_list(request):
    sesiones = Sesion.objects.select_related('paciente', 'Profesional').order_by('-fecha', '-hora')
    return render(request, 'sesion_list.html', {'sesiones': sesiones})

@superuser_required
def sesion_detail(request, pk):
    sesion = get_object_or_404(Sesion, pk=pk)
    return render(request, 'sesion_detail.html', {'sesion': sesion})

@superuser_required
def crear_sesion(request):
    if request.method == 'POST':
        form = SesionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sesión creada exitosamente.')
            return redirect('sesion_list')
    else:
        form = SesionForm()
    return render(request, 'sesion_form.html', {'form': form})

@superuser_required
def editar_sesion(request, pk):
    sesion = get_object_or_404(Sesion, pk=pk)
    if request.method == 'POST':
        form = SesionForm(request.POST, instance=sesion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sesión editada exitosamente.')
            return redirect('sesion_detail', pk=sesion.pk)
    else:
        form = SesionForm(instance=sesion)
    return render(request, 'sesion_form.html', {'form': form, 'sesion': sesion})

@superuser_required
def eliminar_sesion(request, pk):
    sesion = get_object_or_404(Sesion, pk=pk)
    if request.method == 'POST':
        sesion.delete()
        messages.success(request, 'Sesión eliminada exitosamente.')
        return redirect('sesion_list')
    return render(request, 'sesion_confirm_delete.html', {'sesion': sesion})






