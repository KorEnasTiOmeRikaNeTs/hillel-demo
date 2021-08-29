from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class Post(models.Model):
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='post')
	title = models.CharField(max_length=100)
	text = models.TextField()
	slug = models.SlugField(max_length=100, unique=True)
	created_at = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse('home')

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.pk:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)


