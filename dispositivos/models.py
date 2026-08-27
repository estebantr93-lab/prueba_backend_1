from django.db import models


class Dispositivo(models.Model):
    ESTADOS = [
        ("activo", "Activo"),
        ("inactivo", "Inactivo"),
    ]

    nombre = models.CharField(max_length=100)
    zona_id = models.IntegerField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default="activo")
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} (zona {self.zona_id})"
