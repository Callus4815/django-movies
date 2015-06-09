from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Rater(models.Model):
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    occupation = models.IntegerField()
    zipcode = models.IntegerField()

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.Raterid, self.gender, self.age, self.occupation, self.zipcode)




class Movie(models.Model):
    title = models.CharField(max_length=140)




class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.IntegerField()