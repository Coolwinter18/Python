from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    # return HttpResponse('Hola Mundo desde Django')
    no_personas = Persona.objects.count
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('-id')  # +id(default sin signo +) ASC -id DESC || ponga mas de 1 parametro y ordena por primer param, y subordena por 2do param
    return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas': personas})
