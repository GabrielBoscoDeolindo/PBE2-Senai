from rest_framework import serializers
from .models import Pato

class PatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pato
        fields = '__all__'
        read_only_fields = ['id', 'cagaTorrada']