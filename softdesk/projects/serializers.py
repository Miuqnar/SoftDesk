from rest_framework import serializers

from softdesk.users.models import User
from softdesk.users.serializers import UserSignupSerializer
from softdesk.projects.models import (
    Comment, Project,
    Contributor,
    Issue
)


class ProjectSerializer(serializers.ModelSerializer):
    author = UserSignupSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description',
                  'type', 'created_time', 'author')

    # def validate(self, data):
    #     user = self.context['request'].user
    #     if not user.is_staff:
    #         raise serializers.ValidationError("
    # Vous n'êtes pas autorisé à effectuer cette action.")
    #     return data

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class ContributorSerializer(serializers.ModelSerializer):
    user_info = UserSignupSerializer(source='user', read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Contributor
        fields = ('id', 'created_time', 'user', 'user_info')
    
    def validate(self, attrs):
        self.validate_project_exists()
        self.validate_contributor_exists()
        return attrs
        
    def validate_project_exists(self):
        project_id = self.context['view'].kwargs['project_id']
        try:
            Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            raise serializers.ValidationError(
                "Le projet n'existe pas."
                )

    def validate_contributor_exists(self):
        project_id = self.context['view'].kwargs['project_id']
        user = self.initial_data['user']
        if Contributor.objects.filter(project_id=project_id, user=user).exists():
            raise serializers.ValidationError(
                'Le contributeur existe déjà pour ce projet.'
                )

    def create(self, validated_data):
        project = self.context['view'].project
        validated_data['project'] = project
        return super().create(validated_data)


class IssueDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    assigned_to = serializers.StringRelatedField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Issue
        fields = ('id', 'title', 'description', 'priority',
                  'tag', 'status', 'created_time',
                  'author', 'assigned_to', 'comments')

    def get_comments(self, instance):
        queryset = instance.comments.all()
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data
    
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        validated_data['project'] = self.context['project']
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ('uuid', 'author', 'created_time', 'description')

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        validated_data['issue'] = self.context['issue']
        return super().create(validated_data)


class ProjectDetailSerializer(serializers.ModelSerializer):
    contributors = ContributorSerializer(many=True, read_only=True)
    issues = IssueDetailSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    author = UserSignupSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('name', 'description', 'type', 'created_time',
                  'author', 'contributors', 'issues', 'comments')
        