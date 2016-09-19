from __future__ import unicode_literals

from django.db import models

class Movies(models.Model):
	title = models.CharField(max_length=100)
	genre = models.CharField(max_length=25)
	year = models.IntegerField(max_length=4)
	created_at = models.DateTimeField()
