from django import forms
from kinesiologia.models import Profesional, Paciente, Consulta

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