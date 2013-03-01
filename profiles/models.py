from django.db import models
from django.contrib.auth.models import User
from django_countries import CountryField

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = CountryField()
    url = models.URLField("Website", blank=True)
    organization = models.CharField(max_length=50, blank=True)

