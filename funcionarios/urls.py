from django.urls import path
from .views import home, FuncionariosList

urlpatterns = [
    path('', home),
    # path(
    #     'funcionarios',
    #     FuncionariosList.as_view(),
    #     name='list_funcionarios'
    # ),
]