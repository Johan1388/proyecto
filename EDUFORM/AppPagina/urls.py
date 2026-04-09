from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('servicios/', views.test_vocacional, name='servicios'),
    path('resultado/', views.resultado_test, name='resultado'),

    # CRUD
    path('usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),

    path('register/', views.register, name='register'),

    # ✅ AUTENTICACIÓN (CORREGIDO)
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='inicio'   # 🔥 ESTO ES LA CLAVE
    ), name='logout'),
]