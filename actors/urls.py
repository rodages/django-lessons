

from django.urls import path

from actors.views import ActorListView, ActorDetailView


urlpatterns = [
    path('', ActorListView.as_view()),
    path('<int:pk>/', ActorDetailView.as_view())
]
