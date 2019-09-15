from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def clientes(request):
    return render(request, 'clientes.html')
