from rest_framework import viewsets, permissions

from softdesk.projects.models import Contributor, Issue, Project, Comment
from softdesk.projects.permissions import IsProjectContributor, IsAuthorOrReadOnly
from softdesk.projects.serializers import (ContributorSerializer,
                                           CommentSerializer,
                                           IssueDetailSerializer,
                                           ProjectDetailSerializer,
                                           ProjectSerializer, )



class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectContributor]

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectContributor]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Contributor.objects.filter(project_id=project_id)


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Issue.objects.filter(project_id=project_id)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        issue_id = self.kwargs['issue_id']
        return Comment.objects.filter(issue_id=issue_id)