from django import forms

from masterApp.models import User

class LoginForm(forms.Form):

	email = forms.EmailField(label ='',widget=forms.TextInput(
		attrs={'placeholder': 'Email','class':'input100'}))
	password = forms.CharField(label ='',widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'input100'}))
	# email = forms.EmailField()
	# password = forms.CharField()
	def validate_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		if not email.endswith("com"):
			raise forms.ValidationError("This is not a valid email address")
		else:
			return email

class ForgetPassForm(forms.Form):
	email = forms.EmailField(label ='',widget=forms.TextInput(attrs={'placeholder': 'Email', 'class':'input100'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password', 'class':'input100'}))
	password1 = forms.CharField(label ='',widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'input100'}))
    