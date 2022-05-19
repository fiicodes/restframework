from django.shortcuts import render

from rest_framework import generics
from messageapp import serializers
from django.contrib.auth.models import User
from messageapp.models import messagetb
from rest_framework import permissions

  
   
from rest_framework.response import Response
from rest_framework import status


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

class CustomUserRateThrottle(UserRateThrottle):
    rate= '10/hour'
     
class CustomAuthTokenlogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username':user.username
           

        })
 

class MessageList(generics.ListCreateAPIView):
    throttle_classes = [CustomUserRateThrottle]
    queryset = messagetb.objects.all()
    serializer_class = serializers.MessageSerializer
    

    def perform_create(self, serializer):
        
        serializer.save(owner=self.request.user)
        

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_classes = [CustomUserRateThrottle]
    queryset = messagetb.objects.all()
    serializer_class = serializers.MessageSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
