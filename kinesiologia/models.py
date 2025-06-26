from django.db import models

class Profesional (models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Especialidad = models.CharField(max_length=50)
    Tel = models.CharField(max_length=50)
    Email = models.EmailField()
    matricula = models.IntegerField(default=0)

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

class ExamenFisico(models.Model):
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE, related_name='examen_fisico')
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    presion_arterial = models.CharField(max_length=20)
    movimientos_activos = models.TextField()
    movimientos_pasivos = models.TextField()
    test_neurologicos = models.TextField()
    test_ortopedicos = models.TextField()
    test_neurodinamicos = models.TextField()
    palpacion = models.TextField()
    test_adicionales = models.TextField()
    observaciones_clinicas = models.TextField()

    def __str__(self):
        return f"Examen físico de {self.consulta.Paciente} ({self.consulta.Fecha})"

class Sesion(models.Model):
    paciente  = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='sesiones')
    Profesional = models.ForeignKey(Profesional, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Realizada', 'Realizada'), ('Cancelada', 'Cancelada')], default='Pendiente')
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Sesión de {self.paciente} con {self.Profesional} el {self.fecha} a las {self.hora} - Estado: {self.estado}"