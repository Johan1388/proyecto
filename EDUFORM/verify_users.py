import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppEduform.settings')
django.setup()

from django.contrib.auth.models import User
from AppPagina.models import Resultado

total_usuarios = User.objects.count()
usuarios_con_test = Resultado.objects.values('usuario').distinct().count()

print(f"\n=== REPORTE DE USUARIOS ===")
print(f"Total de usuarios registrados: {total_usuarios}")
print(f"Usuarios con test vocacional completado: {usuarios_con_test}")
print(f"\nDetalle de usuarios creados:")

# Mostrar últimos 10 usuarios creados
usuarios_recientes = User.objects.all().order_by('-id')[:10]
for usuario in usuarios_recientes:
    resultado = Resultado.objects.filter(usuario=usuario).first()
    area = resultado.area.nombre if resultado else "Sin test"
    print(f"  - {usuario.username} ({usuario.email}): {area}")
