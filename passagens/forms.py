from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classes

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    ida = forms.DateField(label='Ida',widget=DatePicker())
    volta = forms.DateField(label='Volta',widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da Pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classes)
    informacoes = forms.CharField(
        label="Informações Extras",
        widget=forms.Textarea(),
        max_length=200,
        required=False
    )
    email = forms.EmailField(label='Email')