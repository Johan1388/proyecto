from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import re


# =========================
# FORMULARIO REGISTRO
# =========================
class FormularioRegistro(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico'
        })
    )

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        })
    )

    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña (mínimo 8 caracteres)'
        })
    )

    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirma tu contraseña'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo ya está registrado.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este usuario ya existe.')

        if len(username) < 3:
            raise forms.ValidationError('Debe tener al menos 3 caracteres.')

        if not re.match(r'^[a-zA-Z0-9_.-]+$', username):
            raise forms.ValidationError('Solo letras, números, puntos y guiones.')

        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 8:
            raise forms.ValidationError('Mínimo 8 caracteres.')

        if password1.isdigit():
            raise forms.ValidationError('No puede ser solo números.')

        if password1.isalpha():
            raise forms.ValidationError('Debe tener letras y números.')

        return password1

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return cleaned_data


# =========================
# FORMULARIO EDITAR USUARIO
# =========================
class UsuarioForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']


# =========================
# FORMULARIO LOGIN
# =========================
class FormularioLogin(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Usuario'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
    )