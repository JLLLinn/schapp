import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    """docstring for Question"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # only for python 3, use str. If 2 then use unicode
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # These following 3 lines are for list view to display and sort
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
