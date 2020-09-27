from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def bienvenido(request):
    #return HttpResponse('Hola Mundo desde Django')
    return render(request, 'bienvenido.html')

def despedirse(request):
    return HttpResponse('Despedida desde Django')


def contacto(request):
    return HttpResponse('un Contacto ')