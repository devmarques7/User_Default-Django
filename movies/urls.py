from django.urls import path
from . import views

urlpatterns = [
    path("movies/", views.MovieAssets.as_view()),
    path("movies/<int:movie_id>/", views.MovieAssetsPro.as_view()),
    path("movies/<int:movie_id>/orders/", views.MovieOrderAssets.as_view()),
]
