from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=200, primary_key=True)
    details = models.CharField(max_length=300)
    def __str__(self):              # __unicode__ on Python 2
    	return self.category_name

class SoundEffect(models.Model):
	sid = models.CharField(max_length=8, primary_key=True)
	sound_name = models.CharField(max_length=200)
	date_added = models.DateTimeField('date added')
	tags = models.CharField(max_length=300)
	sound_file = models.CharField(max_length=100, default='none')
	category = models.ForeignKey(Categories)
	def __str__(self):              # __unicode__ on Python 2
		return self.sound_name