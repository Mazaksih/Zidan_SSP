from django.forms import ModelForm
from paket.models import Barang
from django import forms

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'

        widgets = {
            'kodebrg':forms.TextInput({'class':'form-control'}),
            'nama':forms.TextInput({'class':'form-control'}),
            'stok':forms.NumberInput({'class':'form-contro l'}),
            'harga':forms.NumberInput({'class':'form-contro l'}),
            'link_gbr':forms.TextInput({'class':'form-contro l'}),
            'jenis_id':forms.Select({'class':'form-contro l'}),
        }