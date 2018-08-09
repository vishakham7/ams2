from django import forms

from masterApp.models import User

class CreateUserForm(forms.Form):
	name  		= forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Name", "style":""}))
	email 		= forms.EmailField(label='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Email-id"}))
	password 	= forms.CharField(label='', min_length=4, widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
	emp_id  	= forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Employee id", "style":""}))
	thumb_id 	= forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Thumb id"}))
	team 		= forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Team"}))
	shift_id	= forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Shift"}))
	paid_leaves = forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Number of paid leaves", "style":""}))
	user_type 	= forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"User type"}))


class UpdateUserForm(forms.ModelForm):
	# name  		= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Name", "style":""}))
	# email 		= forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Email-id"}))
	# password 	= forms.CharField(min_length=4, widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
	# emp_id  	= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Employee id", "style":""}))
	# thumb_id 	= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Thumb id"}))
	# team 		= forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Team"}))
	shift_id	= forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Shift"}))
	paid_leaves = forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Number of paid leaves", "style":""}))
	user_type 	= forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"User type"}))

	class Meta:
		model = User
		fields = [
			# 'name',
			# 'email',
			# 'password',
			# 'emp_id',
			# 'thumb_id',
			# 'team',
			'shift_id',
			'paid_leaves',
			'user_type',
		]						

	
	