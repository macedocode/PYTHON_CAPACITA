from django.db import models
from django.contrib.auth.models import User

# Define o modelo Customer (isso vira uma tabela no banco de dados)
# Relacionamento 1 para 1 com o usuário do Django
    # Cada cliente pode estar associado a apenas um usuário
class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, # impede deletar o usuário se estiver vinculado
        blank=True, null=True,
        related_name='customer',
        verbose_name='Usuário',
    
    )
    # Nome do cliente
    name = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.CharField(
        max_length=15, 
        blank=True, 
        null=True,
        verbose_name='CPF',
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone',
    )
     # Data de criação do registro
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
    )
     # Data de atualização do registro
    updated_at = models.DateTimeField(
        auto_now=True, # atualiza automaticamente sempre que o registro for salvo
        verbose_name='Atualizado em',
    )

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    def __str__(self):
        return self.name