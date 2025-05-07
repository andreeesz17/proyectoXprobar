from django.shortcuts import render, redirect
from .models import Balon
from .forms import RegistroForm

def inicio(request):
    balones = Balon.objects.all()
    return render(request, 'tienda/inicio.html', {'balones': balones})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'tienda/registro.html', {'form': form})
