import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    """docstring for Question"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #only for python 3, use str. If 2 then use unicode
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
