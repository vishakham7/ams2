from django import forms

from masterApp.models import User

class LoginForm(forms.Form):
	error_css_class = 'error'
	class Meta:
		model = User
		fields = ('email','password')

	email = forms.EmailField(label ='',widget=forms.TextInput(
		attrs={'autocomplete':'off','autofocus':'on','placeholder': 'Email','class':'input100'}))
	password = forms.CharField(label ='',widget=forms.PasswordInput(attrs={'autocomplete':'off','placeholder': 'Password','class':'input100'}))

	# email = forms.EmailField()
	# password = forms.CharField()
	def clean_email(self):
		clean_email = self.cleaned_data.get("email")
		email = User.objects.filter(email=clean_email)
		if not email:
			raise forms.ValidationError("Invalid email address or password")
		else:
			return email

	def clean_password(self):
		clean_password = self.cleaned_data.get("password")
		password = User.objects.filter(password=clean_password)
		if not password:
			raise forms.ValidationError("Invalid email address or password")
		else:
			return password


class ForgetPassForm(forms.Form):
	# error_messages = {
 #        'password_mismatch': ("The two password fields didn't match."),
 #    }
	email = forms.EmailField(label ='',widget=forms.TextInput(attrs={'autocomplete':'off','autofocus':'on','placeholder': 'Email', 'class':'input100'}))
	def clean_email(self):
		clean_email = self.cleaned_data.get("email")
		email = User.objects.filter(email=clean_email)
		if not email:
			raise forms.ValidationError("Invalid email address")
		else:
			return email


class ResetPasswordForm(forms.Form):

	password = forms.CharField(label = '', widget=forms.PasswordInput(attrs={'autocomplete':'off','autofocus':'on','placeholder': 'Repeat Password', 'class':'input100'}))
	password1 = forms.CharField(label ='',widget=forms.PasswordInput(attrs={'autocomplete':'off','placeholder': 'Password','class':'input100'}))

	def clean_password(self):
		password = self.cleaned_data.get('password')
		password1 = self.cleaned_data.get('password1')
		if password and password1:
			if password != password1:
				raise ValidationError("password unmatch")
		
		return password1


	# def save(self, commit=True):
	#     # self.user.set_password(self.cleaned_data['password2'])
	#     self.user.password = password2
	#     if commit:
	#         self.user.save()

	#     return self.user