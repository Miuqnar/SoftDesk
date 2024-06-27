from rest_framework import routers

from softdesk.projects.views import (
    ProjectViewSet,
    ContributorViewSet,
    IssueViewSet, CommentViewSet
)

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

issue_router = routers.SimpleRouter()
issue_router.register(r'issues', IssueViewSet, basename='issues')

comment_router = routers.SimpleRouter()
comment_router.register(r'comments', CommentViewSet, basename='comments')

contributor_router = routers.SimpleRouter()
contributor_router.register(r'contributors',
                            ContributorViewSet, basename='contributors')
