from typing import Sequence
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django_tables2 import SingleTableView
from .forms import TableForm
from django.http import HttpResponse

class PersonListView(SingleTableView):
    model = Usuario
    #template_name = 'tutorial/people.html'
    template_name = 'templates/index.html'
# Create your views here.
class IndexView(ListView):
    template_name='templates/index.html'
    context_object_name= 'usuario_list'
    def get_queryset(self):
        return Usuario.objects.all().select_related('rol')

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'templates/usuario-detail.html'

def create(request):
        if request.method == 'POST':
            form = TableForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('index')
        form = TableForm()
        return render(request,'templates/create.html', {'form':form})

def edit(request, pk, template_name='templates/edit.html'):
        usuario = get_object_or_404(Usuario, pk=pk)
        form = TableForm(request.POST or None, instance = usuario)
        if form.is_valid():
            form.save()
            return redirect('index')    
        return render(request, template_name, {'form': form})

def delete(request, pk, template_name='templates/confirm_delete.html'):
        usuario = get_object_or_404(Usuario, pk=pk)
        if request.method == 'POST':
            usuario.delete()
            return redirect('index')
        return render(request, template_name, {'object':usuario})        
        