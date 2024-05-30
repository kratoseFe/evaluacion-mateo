from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    ficha = models.IntegerField()
    edad = models.IntegerField()
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'estudiante'
        verbose_name_plural = 'estudiantes'
        
    def __str__(self):
        return self.nombre
