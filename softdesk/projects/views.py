from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from softdesk.projects.models import Contributor, Issue, Project, Comment
from softdesk.projects.serializers import (ContributorSerializer,
                                           CommentSerializer,
                                        #    IssueListSerializer,
                                           IssueDetailSerializer,
                                           ProjectDetailSerializer,
                                           ProjectListSerializer, )




class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()



class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Contributor.objects.filter(project_id=project_id)


class IssueViewSet(ModelViewSet):
    # serializer_class = IssueListSerializer
    # detail_serializer_class = IssueDetailSerializer
    serializer_class = IssueDetailSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Issue.objects.filter(project_id=project_id)

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return self.detail_serializer_class
    #     return super().get_serializer_class()


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        issue_id = self.kwargs['issue_id']
        return Comment.objects.filter(issue_id=issue_id)