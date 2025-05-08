from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # prof
    path('professores/', ProfessorListCreateView.as_view(), name='professor-list-create'),
    path('professores/<int:pk>/', ProfessorDetailView.as_view(), name='professor-detail'),

    # disc
    path('disciplinas/', DisciplinaListCreateView.as_view(), name='disciplina-list-create'),
    path('disciplinas/<int:pk>/', DisciplinaDetailView.as_view(), name='disciplina-detail'),

    # ambientes da silva
    path('reservas/', ReservaAmbienteListCreateView.as_view(), name='reserva-list-create'),
    path('reservas/<int:pk>/', ReservaAmbienteDetailView.as_view(), name='reserva-detail'),

    # disciplinas e ambientes espcificos do professor
    path('professores/<int:pk>/disciplinas/', DisciplinasDoProfessorView.as_view(), name='disciplinas-do-professor'),
    path('professores/<int:pk>/reservas/', ReservasDoProfessorView.as_view(), name='reservas-do-professor'),

    # auth auth authhhh
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]