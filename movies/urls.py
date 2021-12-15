from django.urls import path
from movies.views import MovieView, ActorView

urlpatterns = [
    path('movie', MovieView.as_view()),
    path('actor', ActorView.as_view()),
]
