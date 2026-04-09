from django.contrib import admin
from .models import AreaVocacional, Carrera, Pregunta, Resultado


# AREA VOCACIONAL
@admin.register(AreaVocacional)
class AreaVocacionalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


# CARRERA
@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo', 'area')
    list_filter = ('tipo', 'area')
    search_fields = ('nombre',)


# PREGUNTA
@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto', 'area')
    list_filter = ('area',)
    search_fields = ('texto',)


# RESULTADOS (NUEVO 2.0)
@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'area', 'fecha')
    list_filter = ('area', 'fecha')
    search_fields = ('usuario__username',)
    ordering = ('-fecha',)