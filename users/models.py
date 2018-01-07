from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	github_un = models.CharField(max_length=100)

	def __str__(self):
		return self.github_un
