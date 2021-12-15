import json

from django.http import JsonResponse
from django.views import View
from movies.models import Movie, Actor

class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        result = []

        for movie in movies:
            result.append({
                'title': movie.title,
                'running_time': movie.running_time,
                'actors': [actor for actor in movie.actor.values('id', 'last_name')]
            })

        return JsonResponse({'result': result}, status=200)

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        result = []

        for actor in actors:
            result.append({
                'first_name': actor.first_name,
                'last_name': actor.last_name,
                'movies': [movie for movie in actor.movie_set.values('id', 'title')]
            })

        return JsonResponse({'result': result}, status=200)
