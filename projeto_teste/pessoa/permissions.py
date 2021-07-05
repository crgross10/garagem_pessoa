from rest_framework import permissions
from .models import Pessoa

class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        user = Pessoa.objects.get(id_user=request.user)
        if user.tipo == 0:
            return True
        else:
            return False    
