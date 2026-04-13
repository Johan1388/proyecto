from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.paginator import Paginator
import json

from .models import Carrera, Resultado, AreaVocacional, Pregunta
from .forms import UsuarioForm, FormularioRegistro, PreguntaForm


@staff_member_required
def admin_dashboard(request):
    """Dashboard de administración principal"""
    usuarios_count = User.objects.count()
    preguntas_count = Pregunta.objects.count()
    areas_count = AreaVocacional.objects.count()
    resultados_count = Resultado.objects.count()
    
    return render(request, 'paginas/admin_dashboard.html', {
        'usuarios_count': usuarios_count,
        'preguntas_count': preguntas_count,
        'areas_count': areas_count,
        'resultados_count': resultados_count,
    })


# ======================
# INICIO
# ======================
def inicio(request):
    return render(request, 'paginas/inicio.html')


# ======================
# TEST
# ======================
@login_required
def test_vocacional(request):
    return render(request, "paginas/servicios.html")


# ======================
# RESULTADO
# ======================
@login_required
def resultado_test(request):

    if request.method == "POST":

        data = request.POST.get("resultados")

        if not data:
            return redirect("servicios")

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

    return redirect("servicios")


# ======================
# REGISTRO
# ======================
def register(request):

    if request.method == 'POST':
        form = FormularioRegistro(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = FormularioRegistro()

    return render(request, 'paginas/register.html', {'form': form})


# ======================
# LISTAR USUARIOS
# ======================
@staff_member_required
def gestion_usuarios(request):
    usuarios_list = User.objects.all()
    preguntas_list = Pregunta.objects.all().select_related('area').order_by('area', 'id')
    
    # Paginación de usuarios
    paginator_usuarios = Paginator(usuarios_list, 10)
    page_usuarios = request.GET.get('page_usuarios', 1)
    usuarios = paginator_usuarios.get_page(page_usuarios)
    
    # Paginación de preguntas
    paginator_preguntas = Paginator(preguntas_list, 10)
    page_preguntas = request.GET.get('page_preguntas', 1)
    preguntas = paginator_preguntas.get_page(page_preguntas)
    
    return render(request, 'paginas/gestion_usuarios.html', {
        'usuarios': usuarios,
        'preguntas': preguntas,
        'paginator_usuarios': paginator_usuarios,
        'paginator_preguntas': paginator_preguntas,
        'page_usuarios': page_usuarios,
        'page_preguntas': page_preguntas,
    })


# ======================
# EDITAR USUARIO
# ======================
@login_required
def editar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)

    if not request.user.is_staff and request.user != usuario:
        raise PermissionDenied

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
@login_required
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)

    if not request.user.is_staff and request.user != usuario:
        raise PermissionDenied

    if request.method == "POST":
        usuario.delete()
        return redirect('gestion_usuarios')

    return render(request, 'paginas/eliminar_usuario.html', {
        'usuario': usuario
    })


# ======================
# API - PREGUNTAS TEST
# ======================
def obtener_preguntas_test(request):
    """
    Devuelve las preguntas del test en formato JSON
    obtenidas directamente de la base de datos
    """
    preguntas = Pregunta.objects.all().select_related('area')
    
    datos = {
        'preguntas': [],
        'areas': []
    }
    
    areas_dict = {}
    
    for pregunta in preguntas:
        area_nombre = pregunta.area.nombre
        
        # Agregar pregunta
        datos['preguntas'].append({
            'texto': pregunta.texto,
            'area': area_nombre
        })
        
        # Agregar área si no existe
        if area_nombre not in areas_dict:
            areas_dict[area_nombre] = True
            datos['areas'].append(area_nombre)
    
    return JsonResponse(datos)


# ======================
# CRUD PREGUNTAS
# ======================
@staff_member_required
def gestion_preguntas(request):
    """Listar todas las preguntas"""
    preguntas = Pregunta.objects.all().select_related('area').order_by('area', 'id')
    return render(request, 'paginas/gestion_preguntas.html', {
        'preguntas': preguntas
    })


@staff_member_required
def crear_pregunta(request):
    """Crear una nueva pregunta"""
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_preguntas')
    else:
        form = PreguntaForm()

    return render(request, 'paginas/crear_pregunta.html', {
        'form': form
    })


@staff_member_required
def editar_pregunta(request, pk):
    """Editar una pregunta existente"""
    pregunta = get_object_or_404(Pregunta, pk=pk)

    if request.method == 'POST':
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            form.save()
            return redirect('gestion_preguntas')
    else:
        form = PreguntaForm(instance=pregunta)

    return render(request, 'paginas/editar_pregunta.html', {
        'form': form,
        'pregunta': pregunta
    })


@staff_member_required
def eliminar_pregunta(request, pk):
    """Eliminar una pregunta"""
    pregunta = get_object_or_404(Pregunta, pk=pk)

    if request.method == "POST":
        pregunta.delete()
        return redirect('gestion_preguntas')

    return render(request, 'paginas/eliminar_pregunta.html', {
        'pregunta': pregunta
    })