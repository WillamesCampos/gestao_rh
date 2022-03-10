from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView

def home(request):
    return HttpResponse('Ola')


class FuncionariosList(ListView):
    pass