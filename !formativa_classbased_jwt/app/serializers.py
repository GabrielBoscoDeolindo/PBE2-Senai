from rest_framework import serializers
from .models import Professor, Disciplina, ReservaAmbiente

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class ReservaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaAmbiente
        fields = '__all__'
