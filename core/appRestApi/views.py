from django.shortcuts import render
from .models import apiModel
from .serializers import apiSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def add_app(request):
    if request.method == 'POST':
        serializer = apiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "app added successfully!", "data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_app(request, id):
    try:
        app = apiModel.objects.get(pk=id)
    except apiModel.DoesNotExist:
        return Response({"error": "App not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = apiSerializer(app)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_app(request, id):
    try:
        app = apiModel.objects.get(pk=id)
    except apiModel.DoesNotExist:
        return Response({"error": "App not found"}, status=status.HTTP_404_NOT_FOUND)

    app.delete()
    return Response({"message": "App deleted successfully!"}, status=status.HTTP_200_OK)