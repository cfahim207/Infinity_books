from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *

# Create your views here.
class BorrowBookViewset(viewsets.ModelViewSet):
    queryset=BorrowBook.objects.all()
    serializer_class=BorrowBookSerializer
    
    def get_queryset(self):
        queryset=super().get_queryset()
        reader_id=self.request.query_params.get('reader_id')
        if reader_id:
            queryset=queryset.filter(reader_id=reader_id)
        return queryset