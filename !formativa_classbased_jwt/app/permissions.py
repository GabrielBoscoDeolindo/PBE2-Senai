from rest_framework.permissions import BasePermission

class Gestor(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Gestores').exists()
