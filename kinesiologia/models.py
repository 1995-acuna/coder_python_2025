from django.db import models

class Profesional (models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Especialidad = models.CharField(max_length=50)
    Tel = models.CharField(max_length=50)
    Email = models.EmailField()

    def __str__(self):
        return f"Profesional: {self.Apellido} {self.Nombre}"
    
class Paciente (models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Fecha_nacimiento = models.DateField()
    DNI = models.CharField(max_length=50)
    Tel = models.CharField(max_length=50)
    Email = models.EmailField()

    def __str__(self):
        return f"Paciente: {self.Apellido} {self.Nombre}"
    
class Consulta (models.Model):
    Profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE) 
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    Fecha = models.DateField()
    Hora = models.TimeField()
    Observaciones = models.TextField(null=True, blank=True)

# ForeignKey significa que una consulta pertenece a un único profesional
# on_delete=models.CASCADE significa que si se elimina un profesional, se eliminan todas las consultas asociadas

    def __str__(self):
        return f"Consulta: {self.Profesional} {self.Paciente}"
    