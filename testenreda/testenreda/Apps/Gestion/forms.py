from django import forms
from testenreda.Apps.Gestion.models import Factura, Licitacion, Contrato


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
            'nombre',
            'fecha',
            'adjunto',
            'licitacion',
            'contrato',
            'precio',
            'iva',
            'total'
        ]
        labels = {
            'nombre': 'Nombre',
            'fecha': 'Fecha',
            'adjunto': 'Adjunto',
            'licitacion': 'Licitaciones',
            'contrato': 'Contrato',
            'precio': 'Precio',
            'iva': 'iva',
            'total': 'total'
        }
        widgets = {
            'nombre': forms.TextInput(attr={'class':'form-control'}),
            'fecha': forms.DateInput(attr={'class':'form-control'}),
            'adjunto': forms.FileInput(attr={'class':'form-control'}),
            'licitacion': forms.Select(attr={'class':'form-control'}),
            'contrato': forms.Select(attr={'class':'form-control'}),
            'precio': forms.TextInput(attr={'class':'form-control'}),
            'iva': forms.TextInput(attr={'class':'form-control'}),
            'total': forms.TextInput(attr={'class':'form-control'}),
        }
