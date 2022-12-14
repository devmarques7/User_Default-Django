from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("users/", views.UserAssets.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/<user_id>/", views.UserAssetsPro.as_view()),
]
