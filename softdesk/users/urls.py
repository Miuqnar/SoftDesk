from rest_framework import routers

from softdesk.users.views import UserSignupViewset

router_user = routers.SimpleRouter()
router_user.register('user', UserSignupViewset, basename='user')

# urlpatterns = router_user.urls
