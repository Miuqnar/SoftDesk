from rest_framework import viewsets, permissions
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from rest_framework.exceptions import NotFound


from softdesk.projects.models import (Contributor, Issue,
                                      Project, Comment)
from softdesk.projects.permissions import (IsProjectContributor,
                                           IsAuthorOrReadOnly)
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
        return Project.objects.filter(
            Q(author=self.request.user) | 
            Q(contributors__user=self.request.user)
        )
        
    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(id=self.kwargs["pk"]).first()
        if not obj:
            raise NotFound("Project not found.")
        self.check_object_permissions(self.request, obj)
        return obj

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
    
    # def perform_create(self, serializer):
    #     project = Project.objects.get(id=self.kwargs['project_id'])
    #     if project.author != self.request.user:
    #         raise PermissionDenied("You are not the author of this project.")
    #     serializer.save(project=project)


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    # def get_queryset(self):
    #     project_id = self.kwargs['project_id']
    #     return Issue.objects.filter(project_id=project_id)
    
    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Issue.objects.filter(
            Q(project__author=self.request.user) |
            Q(project__contributors__user=self.request.user),
            project_id=project_id
        )
    
    def perform_create(self, serializer):
        project = Project.objects.get(id=self.kwargs['project_id'])
        serializer.save(author=self.request.user, project=project)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        issue_id = self.kwargs['issue_id']
        return Comment.objects.filter(issue_id=issue_id)
    
    # def perfom_create(self, serializer):
    #     issue = Issue.objects.filter(id=self.kwargs['issue_id'])
    #     serializer.save(author=self.request.user, issue=issue)
