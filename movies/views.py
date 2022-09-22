from django.shortcuts import render
from django.views.generic.base import View
from.models import Movie

class MoviesView(View):
    """Kinolar ro'yhati"""
    def get(self,request):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies})