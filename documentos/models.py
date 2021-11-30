from django.db import models
from funcionarios.models import Funcionario

class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    dono = models.ForeignKey(
        Funcionario, on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return self.descricao
