from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from .forms import LivroForm


def lista_livros(request):
    query = request.GET.get('q')  
    if query:
        livros = Livro.objects.filter(titulo__icontains=query) 
    else:
        livros = Livro.objects.all()
    
    return render(request, 'livros/lista_livros.html', {'livros': livros, 'query': query})


def novo_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/form_livro.html', {'form': form})


def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/form_livro.html', {'form': form})


def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == "POST":
        livro.delete()
        return redirect('lista_livros')
    return render(request, 'livros/confirma_exclusao.html', {'livro': livro})
