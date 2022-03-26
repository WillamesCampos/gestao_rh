from django.urls import reverse
from django.db import models
from uuid import uuid4

class Empresa(models.Model):
    codigo = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4
    )
    nome = models.CharField(
        max_length=100,
        help_text='Nome da empresa'
    )

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self) -> str:
        return self.nome
