from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
import json

from .models import Carrera, Resultado, AreaVocacional
from .forms import UsuarioForm


# ======================
# INICIO
# ======================
def inicio(request):
    return render(request, 'paginas/inicio.html')


# ======================
# TEST
# ======================
def test_vocacional(request):
    return render(request, "paginas/servicios.html")


# ======================
# RESULTADO
# ======================
def resultado_test(request):

    if request.method == "POST":

        data = request.POST.get("resultados")

        if not data:
            return redirect("test")

        resultados = json.loads(data)

        total = sum(resultados.values()) or 1

        porcentajes = {}
        for area, count in resultados.items():
            porcentajes[area] = round((count / total) * 100, 1)

        porcentajes_ordenados = sorted(
            porcentajes.items(),
            key=lambda x: x[1],
            reverse=True
        )

        area_nombre = porcentajes_ordenados[0][0]

        area_obj = AreaVocacional.objects.filter(
            nombre__iexact=area_nombre
        ).first()

        carreras = Carrera.objects.filter(area=area_obj) if area_obj else []

        if request.user.is_authenticated and area_obj:
            Resultado.objects.create(
                usuario=request.user,
                area=area_obj
            )

        return render(request, "paginas/resultado.html", {
            "area": area_nombre,
            "carreras": carreras,
            "porcentajes": porcentajes_ordenados,
        })

    return redirect("test")


# ======================
# REGISTRO
# ======================
def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('gestion_usuarios')
    else:
        form = UserCreationForm()

    return render(request, 'paginas/register.html', {'form': form})


# ======================
# LISTAR USUARIOS
# ======================
def gestion_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'paginas/gestion_usuarios.html', {
        'usuarios': usuarios
    })


# ======================
# EDITAR USUARIO
# ======================
def editar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('gestion_usuarios')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'paginas/editar_usuario.html', {
        'form': form,
        'usuario': usuario
    })


# ======================
# ELIMINAR USUARIO
# ======================
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        usuario.delete()
        return redirect('gestion_usuarios')

    return render(request, 'paginas/eliminar_usuario.html', {
        'usuario': usuario
    })