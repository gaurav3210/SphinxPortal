from django.db import models
from Contest.models import contest


class user(models.Model):

    userID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=264)
    userName = models.CharField(max_length=264)
    branch = models.CharField(max_length=264)
    path = models.CharField(max_length=264)

    def __str__(self):
        return self.name



class past_contest(models.Model):

    contestID = models.ManyToManyField(contest)
    userID = models.ManyToManyField(user)
    rank = models.IntegerField()
    marks = models.IntegerField()







