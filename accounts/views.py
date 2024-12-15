from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import SocialMediaUser
from .serializers import SocialMediaUserSerializer, RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = SocialMediaUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(LoginView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = SocialMediaUser.objects.get(id=token.user_id)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

class UserDetailView(generics.RetrieveAPIView):
    queryset = SocialMediaUser.objects.all()
    serializer_class = SocialMediaUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    