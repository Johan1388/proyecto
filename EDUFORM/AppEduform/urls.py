from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppPagina.urls')),
    path('accounts/profile/', RedirectView.as_view(url='/'), name='profile_redirect'),
]
