from django.db import models
from django.utils import timezone
# Create your models here.

class Summoner(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    summoner_name = models.CharField(max_length=200)
    summoner_id = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.summoner_name
