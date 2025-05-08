from rest_framework import generics
from .models import Professor, Disciplina, ReservaAmbiente
from .serializers import ProfessorSerializer, DisciplinaSerializer, ReservaAmbienteSerializer
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import Gestor

# -------------------------- prof ---------------
class ProfessorListCreateView(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [Gestor()]
        return [IsAuthenticatedOrReadOnly()]

class ProfessorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [Gestor()]
        return [IsAuthenticatedOrReadOnly()]


# -------------------- disciplina -----------
class DisciplinaListCreateView(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [Gestor()]
        return [IsAuthenticatedOrReadOnly()]

class DisciplinaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [Gestor()]
        return [IsAuthenticatedOrReadOnly()]


# ------------------------ reservas -------------------
class ReservaAmbienteListCreateView(generics.ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer
    def get_permissions(self):
        if self.request.method == 'POST':
            return [Gestor()]
        return [IsAuthenticatedOrReadOnly()]

class ReservaAmbienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [Gestor()]
        return [IsAuthenticatedOrReadOnly()]


# --------------------- disciplinas e reservas especificas de cada professor ------
class DisciplinasDoProfessorView(generics.ListAPIView):
    serializer_class = DisciplinaSerializer
    def get_queryset(self):
        professor_id = self.kwargs['pk']
        return Disciplina.objects.filter(professor_responsavel__id=professor_id)

class ReservasDoProfessorView(generics.ListAPIView):
    serializer_class = ReservaAmbienteSerializer
    def get_queryset(self):
        professor_id = self.kwargs['pk']
        return ReservaAmbiente.objects.filter(professor_responsavel__id=professor_id)

