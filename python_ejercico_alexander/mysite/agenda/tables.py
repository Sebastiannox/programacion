import django_tables2 as tables
from .models import Agenda

class AgendaTable(tables.Table):
    class Meta:
        model = Agenda
        template_name = "django_tables2/bootstrap.html"
        fields = (
            "pac_rut.rut",
            "pac_rut.nombre",
            "pac_rut.apellido",
            "pac_rut.celular",
            )

        
