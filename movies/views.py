from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from.models import Movie
from .forms import ReviewForm

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
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())

