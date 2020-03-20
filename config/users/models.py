from django.db import models
from django.contrib.auth.models import AbstractUser


class UserPlan(models.Model):
	name = models.CharField(max_length=128)
	def __str__(self):
		return self.name

class User(AbstractUser):
	plan = models.ForeignKey('UserPlan',
		on_delete=models.SET_NULL,
		null=True,
		blank=True)
	def __str__(self):
		return f'{self.username}: {self.first_name}'
# Create your models here.
