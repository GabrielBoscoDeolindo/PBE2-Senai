from django.urls import path
from . import views

urlpatterns = [
    path('alunos/', views.listar_alunos),
    path('alunos/<int:pk>', views.detalhe_aluno),
    path('alunos/criar/', views.criar_aluno),
    path('aluno/alterar/<int:pk>', views.alterar_aluno),
    path('aluno/apagar/<int:pk>', views.deletar_informacoes),
    path('fazAlgo/<str:texto>', views.macharete),
]