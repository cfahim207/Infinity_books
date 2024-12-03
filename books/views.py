from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters,pagination


class BooksViewsets(viewsets.ModelViewSet):
    queryset=Books.objects.all()
    serializer_class=BooksSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    filterset_fields =['category']
    
    def create(self,request,*args,**kwargs):
        return super().create(request,*args,**kwargs)
    
    def destroy(self,request,*args,**kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        books = self.get_object()
        serializer = self.get_serializer(books, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        queryset=super().get_queryset()
        id=self.request.query_params.get('id')
        if id:
            queryset=queryset.filter(id=id)
        return queryset
    
class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
        
        