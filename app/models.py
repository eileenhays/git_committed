from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	github_un = models.CharField(max_length=100)

	def __str__(self):
		return self.github_un


class Commitment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	period = models.CharField(max_length=10)
	count_frequency = models.IntegerField(default=0)
	active = models.BooleanField(default=True)
	penalty_cents = models.IntegerField(default=0)

	def __str__(self):
		return '%s per %s' %(self.count_frequency,
							 self.period
							 )


# class GitSummary(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)	
# 	commitment = models.ForeignKey(Commitment, on_delete=models.CASCADE)
# 	start_datetime = models.DateTimeField('period start time')
# 	end_datetime = models.DateTimeField('period end time')
# 	count = models.IntegerField(default=0)
# 	success = models.BooleanField(default=False)
# 	penalty_paid = models.IntegerField(default=0)
