from django import forms


class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    