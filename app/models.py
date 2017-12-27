from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	github_un = models.CharField(max_length=100)


class Commitment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	period = models.CharField(max_length=10)
	count_frequency = models.IntegerField(default=0)
	active = models.BooleanField(default=True)
	penalty_cents = models.IntegerField(default=0)
