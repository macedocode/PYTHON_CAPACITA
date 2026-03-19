from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField
        User, on_delete=models.PROTECT, 
        blank=True, null=True,
        related_name='customer',
        verbose_name='Usuário',
    
    )

