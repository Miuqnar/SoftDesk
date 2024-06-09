from rest_framework import routers

from softdesk.projects.views import (ProjectViewSet,
                                     ContributorViewSet,
                                     IssueViewSet, CommentViewSet)

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

issue_router = routers.SimpleRouter()
issue_router.register(r'issue', IssueViewSet, basename='issue')

comment_router = routers.SimpleRouter()
comment_router.register(r'comment', CommentViewSet, basename='comment')

contributor_router = routers.SimpleRouter()
contributor_router.register(r'contributor',
                            ContributorViewSet, basename='contributor')
