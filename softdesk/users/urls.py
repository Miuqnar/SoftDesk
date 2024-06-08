from rest_framework import routers

from softdesk.users.views import UserSignupViewset

user_router = routers.SimpleRouter()
user_router.register(r'users', UserSignupViewset, basename='users')

