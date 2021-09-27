from django.shortcuts import render
from .forms import PassagemForms
def index(request):
    form = PassagemForms()
    context = {
        'form':form
    }
    return render(request, 'index.html', context)