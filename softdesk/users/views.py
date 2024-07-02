from rest_framework import viewsets, permissions

from softdesk.users.models import User
from softdesk.users.serializers import UserSignupSerializer
from softdesk.users.permissions import IsAuthenticatedAndOwner


class UserSignupViewset(viewsets.ModelViewSet):
    serializer_class = UserSignupSerializer

    def get_queryset(self):
        queryset = User.objects.filter(id=self.request.user.id)
        return queryset

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [permissions.AllowAny]
        else:
            if self.action in ['update', 'partial_update', 'destroy', 'retrieve']:
                self.permission_classes = [
                    permissions.IsAuthenticated, 
                    IsAuthenticatedAndOwner]
            
        return super().get_permissions()