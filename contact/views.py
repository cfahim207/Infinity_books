from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact
from .serializer import ContactSerializer
# Create your views here.

class ContactViewset(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer
    