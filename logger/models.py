# coding:utf8

from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Log(models.Model):
	what_to_do = models.CharField(max_length=200, blank = False)
	date = models.DateTimeField('date what to do')
	private = models.BooleanField(default = False)
	pub_date = models.DateTimeField('date published', auto_now_add = True, editable = False)
	user = models.ForeignKey(User, editable = False)

	def __unicode__(self):
		return self.what_to_do
		
	def get_current_user():
		return request.user

class LogAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'what_to_do', 'date', 'private', 'user']
	list_display = ('what_to_do', 'pub_date')
    
	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()
	
	was_published_today.short_description = 'Published today?'

admin.site.register(Log)
#admin.site.register(LogAdmin)
