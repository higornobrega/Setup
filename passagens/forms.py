from django import forms


class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    ida = forms.CharField(label='Ida', max_length=100)
    volta = forms.CharField(label='Volta', max_length=100)