from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from softdesk.users.urls import router_user
from softdesk.projects.urls import (router, issue_router,
                                    router_comment, 
                                    contributor_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/projects/<int:project_id>/', include(issue_router.urls)),
    path('api/projects/<int:project_id>/', include(contributor_router.urls)),
    path('api/projects/<int:project_id>/issue/<int:issue_id>/', include(router_comment.urls)),
]

