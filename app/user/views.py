from rest_framework import generics,authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer,AuthTokenSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class=UserSerializer #automatically create user in DB from serializer

class CreateTokenView(ObtainAuthToken):
    """create a new auth token for user"""
    serializer_class=AuthTokenSerializer
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class=UserSerializer
    authentication_classes=(authentication.TokenAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)

    def get_object(self): #when this is called, the self.request has user.and authentication_classes takes cre of authentication of that user.so that user must be authenticated to use API
        """Retrieve  and return authentication user"""
        return self.request.user
