from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal


class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    ]

    numero_pedido = models.CharField(max_length=20, unique=True)
    cliente = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    valor_total = models.DecimalField(
        max_digits=12, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.numero_pedido} - {self.cliente}"