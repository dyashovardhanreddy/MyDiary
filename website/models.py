from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# # Create your models here.

class Diary(models.Model):
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	title =models.CharField(max_length=50)
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	image = models.ImageField(default='diary_thumbnail.jpg',upload_to='diary_thumbnail')

	def __str__(self):
		return self.title
	