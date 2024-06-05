from rest_framework.viewsets import ModelViewSet

from softdesk.users.models import User
from softdesk.users.serializers import UserSignupSerializer


class UserSignupViewset(ModelViewSet):
    serializer_class = UserSignupSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
