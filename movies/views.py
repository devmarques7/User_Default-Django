from .models import Movie
from django.shortcuts import get_object_or_404
from .permissions import MoviePermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Response, Request, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import MovieOrderSerializer, MovieSerializer, SearchMovieSerializer


class MovieAssets(APIView, PageNumberPagination):

    authentication_classes = [JWTAuthentication]
    permission_classes = [MoviePermission]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        page = self.paginate_queryset(movies, request)
        serializer = SearchMovieSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class MovieAssetsPro(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [MoviePermission]

    def get(self, request: Request, movie_id) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = SearchMovieSerializer(movie)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        pet = get_object_or_404(Movie, id=movie_id)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderAssets(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int) -> Response:
        movie_obj = get_object_or_404(Movie, id=movie_id)
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie_obj, buyer=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)
