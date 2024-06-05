from rest_framework import serializers


from softdesk.users.serializers import UserSignupSerializer
from softdesk.projects.models import (Comment, Project,
                                      Contributor,
                                      Issue)


class ProjectListSerializer(serializers.ModelSerializer):
    author =  UserSignupSerializer(read_only=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'type', 'created_time', 'author')
        
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class ContributorSerializer(serializers.ModelSerializer):
    user =  UserSignupSerializer(read_only=True)
    project = ProjectListSerializer()
    class Meta:
        model = Contributor
        fields = ('id', 'created_time', 'user', 'project')


# class IssueListSerializer(serializers.ModelSerializer):
#     # project = ProjectListSerializer()
#     # assigned_to = ContributorSerializer()
#     class Meta:
#         model = Issue
#         fields = ('id', 'title', 'description', 'priority',
#                   'tag', 'status', 'created_time',
#                   'author', 'project', 'assigned_to')


class IssueDetailSerializer(serializers.ModelSerializer):
    project = ProjectListSerializer()
    assigned_to = ContributorSerializer()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Issue
        fields = ('id', 'title', 'description', 'priority',
                  'tag', 'status', 'created_time',
                  'author', 'project', 'assigned_to', 'comments')

    def get_comments(self, instance):
        queryset = instance.comments.all()
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('uuid', 'created_time', 'description', 'author', 'issue')


class ProjectDetailSerializer(serializers.ModelSerializer):
    contributors = ContributorSerializer(many=True, read_only=True)
    issues = IssueDetailSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    author =  UserSignupSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('name', 'description', 'type', 'created_time',
                  'author', 'contributors', 'issues', 'comments')
