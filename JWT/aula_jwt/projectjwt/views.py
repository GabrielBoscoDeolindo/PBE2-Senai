from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import UserAbs
from rest_framework import serializers

class UserAbsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAbs
        fields = [
            'id',
            'username',
            'email',
            'cargo',
            'telefone',
            'biografia',
            'idade',
            'endereco',
            'escolaridade',
            'animais'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = UserAbs(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    cargo = request.data.get('cargo')
    telefone = request.data.get('telefone')
    biografia = request.data.get('biografia')
    idade = request.data.get('idade')
    endereco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')
    animais = request.data.get('animais')
    
    if not username or not password or not email or not cargo:
        return Response({'erro': 'Informações insuficientes'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(username=username).exists():
        return Response({"erro": "Usuário já existe"}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(email=email).exists():
        return Response({"erro": "Email já existe"}, status=status.HTTP_400_BAD_REQUEST)

    usuario = UserAbs.objects.create_user(
        username=username,
        password=password,
        email=email,
        cargo=cargo,
        telefone=telefone,
        biografia=biografia,
        idade=idade,
        endereco=endereco,
        escolaridade=escolaridade,
        animais=animais,
    )
    return Response({"mensagem": f"Usuário {username} criado com sucesso"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar(request):
    username = request.data.get('username')
    password = request.data.get('password')

    usuario = authenticate(username=username, password=password)

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_200_OK)
    else:
        return Response({"erro": "Usuário ou senha inválidos"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_protegida(request):
    return Response({"mensagem": "Olá, você está autenticado!"}, status=status.HTTP_200_OK)

class UserAbsViewSet(viewsets.ModelViewSet):
    queryset = UserAbs.objects.all()
    serializer_class = UserAbsSerializer
    permission_classes = [IsAuthenticated]
