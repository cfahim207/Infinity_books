from rest_framework import serializers
from .models import *

class BooksSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all()) 
    category_display = serializers.StringRelatedField(many=True, source='category', read_only=True) 
    
    class Meta:
        model=Books
        fields=['id','category','category_display','title','image','writer','published','descriptions']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=False, queryset=Books.objects.all())  # For writing
    books_display = serializers.StringRelatedField(many=False, source='books', read_only=True)  # For reading
    class Meta:
        model=Review
        fields=['id','books','books_display','image','name','body','created','rating']
        
        