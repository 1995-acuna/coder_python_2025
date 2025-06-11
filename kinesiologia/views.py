
from django.shortcuts import render, redirect
from .forms import ProfesionalForm, PacienteForm, ConsultaForm
from django.contrib import messages

def home(request):
    return render(request, 'base.html')

def crear_profesional(request):
    form = ProfesionalForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Profesional guardado exitosamente.")
        return redirect('home')
    return render(request, 'crear_profesional.html', {'form': form})

def crear_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Paciente guardado exitosamente.")
        return redirect('home')
    return render(request, 'crear_paciente.html', {'form': form})

def crear_consulta(request):
    form = ConsultaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'crear_consulta.html', {'form': form})



