from rest_framework import viewsets, permissions

from softdesk.users.models import User
from softdesk.users.serializers import UserSignupSerializer


class UserSignupViewset(viewsets.ModelViewSet):
    serializer_class = UserSignupSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
