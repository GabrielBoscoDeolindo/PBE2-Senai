from rest_framework import serializers
from .models import Pato, DonoDoPato
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class PatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pato
        fields = '__all__'
        read_only_fields = ['id', 'cagaTorrada']

class DonoPatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonoDoPato
        fields = '__all__'
    
class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        dados = super().validate(attrs)
        dados['usuario'] = {
            'nome': self.user.username,
            'bio': self.user.bio
        }
        return dados
