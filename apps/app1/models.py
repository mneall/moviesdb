from __future__ import unicode_literals

from django.db import models

class Movies(models.Model):
	title = models.CharField(max_length=100, )