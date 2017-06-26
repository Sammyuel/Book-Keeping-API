from django.db import models
from django.contrib.auth.models import User
from home.models import Titles
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from django.conf import settings
from datetime import datetime
from decimal import Decimal
from datetime import date
    
class Posts(models.Model):
    titles = models.ForeignKey(Titles,on_delete = models.CASCADE)
    team_1 = models.CharField(max_length=100)
    team_2 = models.CharField(max_length=100)
    bet_ammount = models.BigIntegerField()
    receive_ammount = models.BigIntegerField()
    result = models.BooleanField(default = False)
    profit = models.BigIntegerField(default = 0)
    def __str__(self):
        return self.team_1 + " vs " + self.team_2

class odds(models.Model):
    titles = models.ForeignKey(Titles,on_delete = models.CASCADE)
    team_1 = models.CharField(max_length=100)
    team_2 = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    odds = models.DecimalField(max_digits = 20, decimal_places = 4)
    result = models.CharField(max_length=100)
    def __str__(self):
        return self.team_1 + " vs " + self.team_2

class events(models.Model):
    titles = models.ForeignKey(Titles, on_delete=models.CASCADE)
    event = models.CharField(max_length = 100)
    date = models.DateTimeField(default = datetime.now)
    players = models.CharField(max_length = 100)
    
