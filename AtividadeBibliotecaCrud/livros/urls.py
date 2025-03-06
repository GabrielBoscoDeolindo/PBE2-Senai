from django.urls import path
from .views import lista_livros, novo_livro, editar_livro, excluir_livro

urlpatterns = [
    path('', lista_livros, name='lista_livros'),
    path('novo/', novo_livro, name='novo_livro'),
    path('editar/<int:id>/', editar_livro, name='editar_livro'),
    path('excluir/<int:id>/', excluir_livro, name='excluir_livro'),
]
