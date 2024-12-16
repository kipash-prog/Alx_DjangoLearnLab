from rest_framework import serializers
from .models import Book
from  rest_framework.serializers import ModelSerializer


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self,data):
        if data['name'] is None:
            return serializers.ValidationError("Book is Not Found")

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model=Author
        fields='__all__'
