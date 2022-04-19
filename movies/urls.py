

from django.urls import path

from movies.views import MovieListView, MovieDetailView


urlpatterns = [
    path('', MovieListView.as_view()),
    path('<str:pk>/', MovieDetailView.as_view()),
]
