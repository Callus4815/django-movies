# Create your views here.
from django.db.models import Count
from django.shortcuts import render
from .models import Rater, Rating, Movie
from django.contrib.auth.models import User
from django.http import HttpResponse


def movies(request):
    # movieid = Movie.movies.annotate(Count('id')).order_by('-id__count')
    movieid = Movie.objects.annotate(Count('id').order_by("-id")
    return render(request,
                  'movieLens/movies.html',
                  {"Movies": movieid})


def show_rater(request):
    rater = Rater.objects.all()

    return render(request, 'movieLens/rater.html'[0:20])


def ratinger(request):
    ratings = Rating.objects.annotate(Count('rating'))
    return HttpResponse(ratings[0:20])
