from django.urls import path
from .views import PatoListCreateAPIView, PatoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('patos/', PatoListCreateAPIView.as_view(), name='pato-list-create'),
    path('patos/<int:pk>/', PatoRetrieveUpdateDestroyAPIView.as_view(), name='pato-especifico')
]