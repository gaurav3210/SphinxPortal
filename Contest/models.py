from django.db import models
#from User.models import user

class contest(models.Model):

    date = models.DateField()
    contestName = models.CharField(max_length=264,blank=False,default="Foxtrot")
    contestHost = models.CharField(max_length=264,default="Mike")
    theme=models.CharField(max_length=264,default="Alpha")
    contestID = models.IntegerField(primary_key=True)



class question(models.Model):

    questionID = models.IntegerField(primary_key=True)
    contestID = models.ManyToManyField(contest)
    question = models.CharField(max_length=264)
    answer = models.CharField(max_length=264)

"""
class participants(models.Model):
    userID = models.ManyToManyField(user)
    contestID = models.ManyToManyField(contest)
    rank = models.IntegerField()
"""