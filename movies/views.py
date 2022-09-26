from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from.models import Movie

class MoviesView(ListView):
    """Kinolar ro'yhati"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movie_list.html"


class MovieDetailView(DetailView):
    """Film tavsiflari bilan to'la."""
    model = Movie
    slug_field = "url"


class AddReview(View):
    """sharhlar"""
    def post(self, request, pk):
        print(request.POST)
        return redirect("/")

