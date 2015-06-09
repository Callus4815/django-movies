from django.contrib import admin
from .models import Rater, Movie, Rating


# Register your models here.

class RaterAdmin(admin.ModelAdmin):
    list_display = ['gender', 'age', 'occupation', 'zipcode']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']



class RatingAdmin(admin.ModelAdmin):
    list_display = ['rater', 'movie', 'rating', 'timestamp']








admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
