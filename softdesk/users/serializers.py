from rest_framework import serializers

from softdesk.users.models import User


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'age', 
                  'email', 'can_be_contacted', 
                  'can_data_be_shared')
