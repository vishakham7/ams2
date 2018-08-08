from django.db import models

# Create your models here.

class User(models.Model):
	name 		= models.CharField(max_length=100)
	email 		= models.CharField(max_length=100)
	emp_id 		= models.CharField(max_length=10)
	password 	= models.CharField(max_length=10)
	thumb_id 	= models.CharField(max_length=100, null=True)
	shift_id 	= models.IntegerField(null=True)
	paid_leaves = models.IntegerField()
	team 		= models.IntegerField()
	user_type 	= models.IntegerField()
	del_flag 	= models.IntegerField(default=1)
	

class Shift(models.Model):
	title 		= models.CharField(max_length=50)
	end_time 	= models.CharField(max_length=100)
	start_time 	= models.CharField(max_length=100)


class Holidays(models.Model):
	title 		= models.CharField(max_length=50)
	date 		= models.CharField(max_length=100)


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
	no_of_days 	= models.IntegerField(max_length=20) 


