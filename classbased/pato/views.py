from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Pato
from .serializers import PatoSerializer
# Create your views here.

class PatoListCreateAPIView(ListCreateAPIView):
    queryset = Pato.objects.all()
    serializer_class = PatoSerializer

    