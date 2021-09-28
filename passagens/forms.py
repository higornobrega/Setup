from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classes
from passagens.validation import *

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
    
       
    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        ida = self.cleaned_data.get('ida')
        volta = self.cleaned_data.get('volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_erros = {}
        campo_tem_algum_numero(origem, 'origem', lista_erros)
        campo_tem_algum_numero(destino, 'destino', lista_erros)
        origem_destino_iguais(origem, destino, lista_erros)
        ida_antes_da_volta(ida, volta, lista_erros)
        ida_antes_de_hoje(ida, data_pesquisa, lista_erros)
        if lista_erros is not None:
            for erro in lista_erros:
                mensagem_erro = lista_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data
