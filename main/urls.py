from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunoView, name='alunos-lista'),
    path('alunoID/<int:id>', views.alunoIDview, name='aluno-detalhe'),

]
