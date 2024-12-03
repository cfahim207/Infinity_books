from rest_framework import serializers
from .models import *
from books.models import Books
from readers.models import Reader

class BorrowBookSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=False,queryset=Books.objects.all())  # For writing
    books_display = serializers.StringRelatedField(many=False, source='books', read_only=True)  # For reading
    reader = serializers.PrimaryKeyRelatedField(many=False,queryset=Reader.objects.all())  # For writing
    reader_display = serializers.StringRelatedField(many=False, source='reader', read_only=True)  # For reading
    
    class Meta:
        model= BorrowBook
        fields=['id','books','books_display','reader','reader_display','borrowDate']
        
    