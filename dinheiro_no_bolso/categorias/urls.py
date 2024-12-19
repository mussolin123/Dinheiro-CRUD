from django.urls import path
from .views import CategoriaListView, CategoriaDetailView

urlpatterns = [
    path('', CategoriaListView.as_view(), name='categoria-list-create'),  # GET e POST para lista de categorias
    path('<int:id>/', CategoriaDetailView.as_view(), name='categoria-detail'),  # GET, PUT e DELETE para uma categoria específica
]
