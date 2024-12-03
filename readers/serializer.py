from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ReaderSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)
    class Meta:
        model=Reader
        fields='__all__'
        
class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password= serializers.CharField(write_only=True, required=True)
    image=serializers.CharField(required=False)
    phone=serializers.CharField(required=True)
    address=serializers.CharField(required=True)
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','confirm_password','image','phone','address']
        extra_kwargs={
            'password':{'write_only':True},
        }
        
    def validate(self,data):
        if data['password']!=data['confirm_password']:
            raise serializers.ValidationError("Password does not match")
        return data
    
    def create(self,validated_data):
        username=validated_data['username']
        first_name=validated_data['first_name']
        last_name=validated_data['last_name']
        email=validated_data['email']
        password=validated_data['password']
        image=validated_data.get('image')
        phone=validated_data['phone']
        address=validated_data['address']
        
        
        user=User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        
        user.set_password(password)
        user.is_active=False
        user.save()
        
        Reader.objects.create(
            user=user,
            image=image,
            phone=phone,
            address=address
        )
        
        return user

class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)