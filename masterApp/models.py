from django.db import models
# Create your models here.
from datetime import datetime 
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.sessions.models import Session

class User(models.Model):
	name 		= models.CharField(max_length=100)
	email 		= models.CharField(max_length=100)
	emp_id 		= models.CharField(max_length=10)
	password 	= models.CharField(max_length=100)
	thumb_id 	= models.CharField(max_length=100, null=True)
	shift_id 	= models.IntegerField(null=True)
	paid_leaves = models.IntegerField()
	team 		= models.IntegerField()
	user_type 	= models.IntegerField()
	del_flag 	= models.IntegerField(default=1)

	def __str__(self):
		return self.email

# User.profile = property(lambda u: User.objects.get_or_create(user=u)[0])	

class Shift(models.Model):
	title 		= models.CharField(max_length=50)
	start_time 	= models.CharField(max_length=100)
	end_time 	= models.CharField(max_length=100)
	# del_flag 	= models.IntegerField(default=1)


class Holidays(models.Model):
	title 		= models.CharField(max_length=50)
	date 		= models.CharField(max_length=100, default=datetime.now())


class Attendance(models.Model):
	emp_id 		= models.CharField(max_length=10)
	thumb_id 	= models.CharField(max_length=100)
	date_time 	= models.CharField(max_length=100)
	in_out_flag	= models.CharField(max_length=20) 
	shift_id	= models.IntegerField() 

class Team(models.Model):
	name 		= models.CharField(max_length=20) 

class UserType(models.Model):
	user_type 	= models.CharField(max_length=20) 

class PaidLeaves(models.Model):
	no_of_days 	= models.IntegerField() 


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)