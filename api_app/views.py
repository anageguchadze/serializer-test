from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer

# Create your views here.

from .models import Book

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer