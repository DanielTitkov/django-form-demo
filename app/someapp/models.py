from django.db import models

# Create your models here.

class Huuser(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    goal_in_life = models.CharField(max_length=200, default="who cares") # sorry, cannot change that