from dataclasses import fields
from django.shortcuts import render
from empresas.models import Empresa
from django.views.generic import (
    ListView, CreateView, DeleteView, UpdateView
)


class EmpresaCreate(CreateView):
    model = Empresa
    fields = "__all__"

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario

        funcionario.empresa = obj
        funcionario.save()

        return super().form_valid(form)


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']