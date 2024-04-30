from django.shortcuts import render

# Create your views here.
from api.models import Movie 
from api.serializers import MovieSerializer 
from rest_framework import generics

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer