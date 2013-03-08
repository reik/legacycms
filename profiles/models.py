from django.db import models
from django.contrib.auth.models import User
from django_countries import CountryField

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    country = CountryField()
    url = models.URLField("Website", blank=True)
    organization = models.CharField(max_length=50, blank=True)

    class Meta:
        app_label = 'legacycms'

    def get_absolute_url(self):
        return "/profiles/%s" % self.user.username

