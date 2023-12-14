from django.shortcuts import render

from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from apiaccount.models import User


from apiaccount.serializers import UserSerializer


class UserLoginView(ObtainAuthToken):
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
            )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_serializer = UserSerializer(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {'token': token.key, 'user': user_serializer.data},
            status=status.HTTP_201_CREATED
            )
    
userloginView = UserLoginView.as_view()

class UserLogoutView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        request.auth.delete()
        return Response(
            {"detail": "Successfully logged out."},
            status=status.HTTP_200_OK
            )

userlogoutView = UserLogoutView.as_view()

class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to register

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response(
            {"detail": "Successfully signed in."},
            status=status.HTTP_201_CREATED
            )
        
usersignupView = UserSignupView.as_view()
