from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Movie
from movies.serializers import MovieSerializer

# Create your views here.


class MovieListView(APIView):
    def get(self, _request):
        movies = Movie.objects.all()
        serialized_movies = MovieSerializer(movies, many=True)
        return Response(serialized_movies.data)

    def post(self, request, format=None):
        movie = MovieSerializer(data=request.data)
        if movie.is_valid():
            movie.save()
            return Response(movie.data, status=status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    def get(self, _request, pk):
        movie = Movie.objects.get(id=pk)
        serialized_movie = MovieSerializer(movie, many=False)
        return Response(serialized_movie.data)

    def put(self, request, pk, format=None):
        movie = Movie.objects.get(id=pk)
        serialized_movie = MovieSerializer(movie, data=request.data)
        if serialized_movie.is_valid():
            serialized_movie.save()
            return Response(serialized_movie.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        movie = Movie.objects.get(id=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
