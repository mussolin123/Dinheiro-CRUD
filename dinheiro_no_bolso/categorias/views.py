from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Categoria
from .serializers import CategoriaSerializer


class CategoriaListView(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriaDetailView(APIView):
    def get(self, request, id):
        try:
            categoria = Categoria.objects.get(id=id)
        except Categoria.DoesNotExist:
            return Response({"error": "Categoria não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            categoria = Categoria.objects.get(id=id)
        except Categoria.DoesNotExist:
            return Response({"error": "Categoria não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            categoria = Categoria.objects.get(id=id)
        except Categoria.DoesNotExist:
            return Response({"error": "Categoria não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        categoria.delete()
        return Response({"message": "Categoria deletada com sucesso."}, status=status.HTTP_204_NO_CONTENT)
