from multiprocessing import context
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.exceptions import NotFound


from softdesk.projects.models import (
    Contributor, Issue,
    Project, Comment
)
from softdesk.projects.permissions import (
    IsAuthorOrReadOnly,
    IsProjectOwer,
    ProjectPermissions
)
from softdesk.projects.serializers import (
    ContributorSerializer,
    CommentSerializer,
    IssueDetailSerializer,
    ProjectDetailSerializer,
    ProjectSerializer, 
)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [permissions.IsAuthenticated, 
                          ProjectPermissions]


    def get_queryset(self):
        return Project.objects.filter(
            Q(author=self.request.user) | 
            Q(contributors__user=self.request.user)
        ).distinct()
        

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated, 
                          IsProjectOwer]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Contributor.objects.filter(project_id=project_id)
    
    def initial(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=self.kwargs['project_id'])
        super().initial(request, *args, **kwargs)


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueDetailSerializer
    permission_classes = [permissions.IsAuthenticated, 
                          IsAuthorOrReadOnly]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Issue.objects.filter(project_id=project_id)
    

    # def perform_create(self, serializer):
    #     project = Project.objects.get(id=self.kwargs['project_id'])
    #     serializer.save(author=self.request.user, project=project)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, 
                          IsAuthorOrReadOnly]

    def get_queryset(self):
        # import pdb;pdb.set_trace()
        issue_id = self.kwargs['issue_id']
        return Comment.objects.filter(issue_id=issue_id)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['issue'] = Issue.objects.get(id=self.kwargs['issue_id'])
        return context
    
    # def perfom_create(self, serializer):
    #     issue = Issue.objects.get(id=self.kwargs['issue_id'])
    #     # serializer.save(author=self.request.user, issue=issue)
    