from rest_framework import serializers
from django.contrib.auth.models import User
from messageapp.models import messagetb

class MessageSerializer(serializers.ModelSerializer):
    userid = serializers.ReadOnlyField(source='owner.id')

    username = serializers.ReadOnlyField(source='owner.username')
    email = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = messagetb
        fields = ['id', 'messages', 'created_at', 'updated_at','userid','username','email']

   
    
    





class UserSerializer(serializers.ModelSerializer):
    mess = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username','mess']