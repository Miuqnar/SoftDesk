from datetime import timedelta
from time import timezone
from rest_framework import serializers

from softdesk.users.models import User


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'age', 
                  'email', 'password', 'can_be_contacted', 
                  'can_data_be_shared')
        
    def validate_age(self, value):
        if value < 15:
            raise  serializers.ValidationError("Vous devez avoir au moins 15 ans pour s'inscrire")
        return value
    
    def create(self, validated_data):
        # Pop le champ mot de passe pour éviter de le passer dans 
        # les arguments de création d'utilisateur
        # password de validated_data car create_user s'en charge 
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user 
