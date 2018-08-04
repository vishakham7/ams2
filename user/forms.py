from django import forms

from masterApp.models import User

class CreateUserForm(forms.Form):
	name  		= forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Name", "style":""}))
	email 		= forms.EmailField(label='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Email-id"}))
	password= forms.CharField(label='', min_length=4, widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
	emp_id  	= forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Employee id", "style":""}))
	thumb_id 	= forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Thumb id"}))
	team 		= forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Team"}))
	shift_id		= forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Shift"}))
	paid_leaves = forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Number of paid leaves", "style":""}))
	user_type 	= forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"User type"}))