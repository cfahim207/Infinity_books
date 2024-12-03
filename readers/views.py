from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated

# Email importing
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect


# Create your views here.
class ReaderViewset(viewsets.ModelViewSet):
    queryset=Reader.objects.all()
    serializer_class=ReaderSerializer
    
    def get_queryset(self):
        queryset=super().get_queryset()
        id=self.request.query_params.get('id')
        if id:
            queryset=queryset.filter(id=id)
        return queryset
    
class UserRegisterView(APIView):
    serializer_class=RegistrationSerializer
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user=serializer.save()
            token=default_token_generator.make_token(user)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link=f'http://127.0.0.1:8000/reader/active/{uid}/{token}'
            email_subject='Confirm Your Email'
            email_body=render_to_string("confirm_email.html",{'confirm_link': confirm_link})
            email=EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response('Check your mail for confirmation')
        return Response(serializer.errors)
    
def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user=User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
            
            
class UserLoginApiView(APIView):
    def post(self,request):
        serializer=UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            
            user=authenticate(username=username,password=password)
            
            if user:
                token,_=Token.objects.get_or_create(user=user)
                reader,_=Reader.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token':token.key,'user_id':user.id,'reader_id':reader.id})
            
            else:
                return Response({'error':'Invalid Credential'})
            
        return Response(serializer.errors)

        
class UserLogoutApiView(APIView):
    def get(self,request):
        logout(request)
        # request.user.auth_token.delete()
        return redirect('login')
