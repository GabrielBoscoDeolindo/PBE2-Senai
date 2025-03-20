from django.shortcuts import render
from django.shortcuts import render
from .models import Evento
from .serializers import EventoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import date

# Create your views here.

@api_view(['GET'])
def listareventos(request):
    Eventos = Evento.objects.all()
    serializer = EventoSerializer(Eventos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalhe_evento(request, pk):
    try:
        Events = Evento.objects.get(pk=pk)
    except Events.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EventoSerializer(Events)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def filtrar_eventos_proximos(request):
    start_date = date(2025, 3, 27)
    end_date = date(2025, 3, 20)
    Eventos = Evento.objects.filter(data__range=(start_date, end_date))
    serializer = EventoSerializer(Eventos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def criar_evento(request):
    if request.method == 'POST':
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["DELETE"])
def deletar_evento(request, pk):
    try:
        Events = Evento.objects.get(pk=pk)
    except Events.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    Events.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["PUT"])
def editar_evento(request, pk):
    try:
        Events = Evento.objects.get(pk=pk)
    except Events.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EventoSerializer(Events, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)