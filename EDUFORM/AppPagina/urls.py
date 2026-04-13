from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('servicios/', views.test_vocacional, name='servicios'),
    path('resultado/', views.resultado_test, name='resultado'),

    # API
    path('api/preguntas/', views.obtener_preguntas_test, name='api_preguntas'),

    # ADMIN DASHBOARD
    path('admin/', views.admin_dashboard, name='admin_dashboard'),

    # CRUD USUARIOS
    path('usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),

    # CRUD PREGUNTAS
    path('preguntas/', views.gestion_preguntas, name='gestion_preguntas'),
    path('preguntas/crear/', views.crear_pregunta, name='crear_pregunta'),
    path('preguntas/editar/<int:pk>/', views.editar_pregunta, name='editar_pregunta'),
    path('preguntas/eliminar/<int:pk>/', views.eliminar_pregunta, name='eliminar_pregunta'),

    path('register/', views.register, name='register'),

    # AUTENTICACIÓN
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='inicio'
    ), name='logout'),
]