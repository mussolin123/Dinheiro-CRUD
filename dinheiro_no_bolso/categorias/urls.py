from django.urls import path
from .views import CategoriaListView, CategoriaDetailView

urlpatterns = [
    path('', CategoriaListView.as_view(), name='categoria-list-create'),
    path('<int:id>/', CategoriaDetailView.as_view(), name='categoria-detail'),
]
