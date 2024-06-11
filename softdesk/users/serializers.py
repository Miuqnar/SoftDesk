from rest_framework import serializers

from softdesk.users.models import User


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'age',
                  'email', 'password', 'can_be_contacted',
                  'can_data_be_shared')

    def validate_age(self, value):
        if value < 15:
            raise serializers.ValidationError(
                "Vous devez avoir au moins 15 ans pour s'inscrire"
            )
        return value

    def create(self, validated_data):

        """
        Pop le champ mot de passe pour éviter de le
        passer dansles arguments de création d'utilisateur
        password de validated_data car create_user s'en charge
        """

        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.is_active = True
        if password is not None:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

    # def delete(self, instance):
    #     instance.delete()
    #     return instance
