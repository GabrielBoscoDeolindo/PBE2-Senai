from django.urls import path
from . import views

urlpatterns = [
    path('listar_eventos/', views.listareventos),
    path('criar_evento/', views.criar_evento),
    path('editar_evento/<int:pk>', views.editar_evento),
    path('deletar_evento/<int:pk>', views.deletar_evento),
    path('detalhe_evento/<int:pk>', views.detalhe_evento),
    path('filtrar_eventos/', views.filtrar_eventos_proximos)
]