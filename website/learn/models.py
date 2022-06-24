from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save

class LearnerUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	is_admin = models.BooleanField(default=False, null=False)

	class Meta:
		verbose_name_plural = 'Users'

	def __str__(self):
		return self.user.username



