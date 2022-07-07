from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save

class LearnerUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	is_user_admin = models.BooleanField(default=False, null=False)

	class Meta:
		verbose_name_plural = 'Users'

	def __str__(self):
		return self.user.username



# Subtopics should inherit from topics.
# Subtopics should have a parent property at all times.

class Topic(models.Model):
	topic_name = models.TextField(max_length=100)
	topic_icon = models.ImageField(upload_to=f'/static/images/{topic_name}/')

	class Meta:
		verbose_name_plural = 'Topics'

	def __str__(self):
		return self.topic_name


class Subtopic(models.Model): 
	...







