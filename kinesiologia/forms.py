from django import forms
from kinesiologia.models import Profesional, Paciente, Consulta, ExamenFisico, Sesion

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = "__all__" # todos los campos

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = "__all__" # todos los campos

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = "__all__"

class ExamenFisicoForm(forms.ModelForm):
    class Meta:
        model = ExamenFisico
        exclude = ['consulta']
        widgets = {
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'altura': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'presion_arterial': forms.TextInput(attrs={'class': 'form-control'}),
            'movimientos_activos': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'movimientos_pasivos': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'test_neurologicos': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'test_ortopedicos': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'test_neurodinamicos': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'palpacion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'test_adicionales': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'observaciones_clinicas': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class SesionForm(forms.ModelForm):
    class Meta:
        model = Sesion
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'Profesional': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }