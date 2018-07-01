from django.shortcuts import render
from django.views.generic import CreateView

from testenreda.Apps.Gestion.models import Factura, Licitacion, Contrato
from testenreda.Apps.Gestion.forms import FacturaForm
# Create your views here.

class FacturaCreate(CreateView):
    model = Factura
    form_class = FacturaForm
    templte_name = 'Gestion/facturas.htlm'