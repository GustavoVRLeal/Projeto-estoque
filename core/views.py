from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    context={
        'mensagem': 'Bem vindo á aplicação estoqueWeb'
    }
    return(request, template_name, context)
