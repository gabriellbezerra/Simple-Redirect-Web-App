from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
import string
import random
from . import models


# Create your views here.

def main_page(request:HttpRequest):
    return render(request, 'main_page.html')

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_url(request:HttpRequest):
    url = request.POST['URL']
    encurtado = id_generator()

    teste = models.LINK.objects.filter(pk=encurtado)

    if not teste:
        new_link = models.LINK.objects.create(
            original_url = url,
            encurtado_url = encurtado
        )
        context = {
            'encurtado' : encurtado,
        }
        return render(request, 'link_criado.html', context)
    else:
        return redirect('main_page')

def redirection(request:HttpRequest, encurtado):
    teste = models.LINK.objects.filter(pk=encurtado)
    if teste:
        link = models.LINK.objects.get(pk=encurtado)
        url_to_go = link.original_url
        return redirect(url_to_go)
    else:
        return redirect('main_page')
