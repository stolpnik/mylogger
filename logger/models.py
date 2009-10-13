from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Log(models.Model):
	what_to_do = models.CharField(max_length=200)
	date = models.DateTimeField('date what to do')
	private = models.BooleanField(default=False)
	pub_date = models.DateTimeField('date published', auto_now_add = True)
	user = models.ForeignKey(User)
	

	def __unicode__(self):
		return self.what_to_do

