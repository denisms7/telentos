from django.db import models
from skills.models import Function


class AccessRequest(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'

    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pendente'),
        (STATUS_APPROVED, 'Aprovada'),
        (STATUS_REJECTED, 'Rejeitada'),
    )

    email = models.EmailField(unique=True, verbose_name="Email")
    username = models.CharField(max_length=150, unique=True, verbose_name="Usuario")
    full_name = models.CharField(max_length=255, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    role = models.ForeignKey(Function, on_delete=models.PROTECT, related_name="access_requests", verbose_name="Cargo Efetivo",)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING,)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Solicitação de Acesso'
        verbose_name_plural = 'Solicitações de Acesso'

    def __str__(self):
        return f'{self.full_name} ({self.get_status_display()})'
