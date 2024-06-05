from rest_framework import routers

from softdesk.projects.views import (ProjectViewSet,
                                     ContributorViewSet,
                                     IssueViewSet, CommentViewset)

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

issue_router = routers.SimpleRouter()
issue_router.register(r'issue', IssueViewSet, basename='issue')

router_comment = routers.SimpleRouter()
router_comment.register(r'comment', CommentViewset, basename='comment')

contributor_router = routers.SimpleRouter()
contributor_router.register(r'contributor', ContributorViewSet, basename='contributor')

