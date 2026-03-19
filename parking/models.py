from django.db import models
from vehicles.models import Vehicle


# Modelo que representa uma vaga de estacionamento
class ParkingSpot(models.Model):
    spot_number = models.IntegerField(
        unique=True,
        verbose_name='Número de Vaga',
    )
    # Indica se a vaga está ocupada ou livre
    is_occupied = models.BooleanField(
        default=False,
        verbose_name='Ocupado',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return str(self.spot_number)


class ParkingRecord(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name='parking_records',
        verbose_name='Veículo',
    )
   # Relacionamento com a vaga
    parking_spot = models.ForeignKey(
        ParkingSpot,
        on_delete=models.PROTECT,
        related_name='parking_records',
        verbose_name='Vaga',
    )

    entry_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Horário de Entrada',
    )
 # Horário de saída (pode ficar vazio até o carro sair)
    exit_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Horário de Saída',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        return f'{self.vehicle} - {self.parking_spot} - {self.entry_time}'