from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/despesas/', include('despesas.urls')),
    path('api/relatorios/', include('relatorios.urls')),
    path('api/categorias/', include('categorias.urls')),
    path('api/user/', include('user.urls')),  # Incluindo as URLs do app 'user'
]
