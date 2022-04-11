from django.shortcuts import render
from django_tables2 import SingleTableView
from .models import Agenda, Doctor
from .tables import AgendaTable
from django.views.generic import ListView, DetailView

# Create your views here.
class IndexView(ListView):
    template_name="templates/agenda.html"
    context_object_name= 'agenda_list'
    def get_queryset(self):
        return Agenda.objects.all()
    

