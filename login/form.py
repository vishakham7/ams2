from django import forms

from masterApp.models import User

class LoginForm(forms.Form):
	class Meta:
		model = User
		fields = ('email','password')

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
	error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
	email = forms.EmailField(label ='',widget=forms.TextInput(attrs={'placeholder': 'Email', 'class':'input100'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password', 'class':'input100'}))
	password1 = forms.CharField(label ='',widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'input100'}))
    
	

	def clean_new_password2(self):
	    password1 = self.cleaned_data.get('new_password1')
	    password2 = self.cleaned_data.get('new_password2')
	    if password1 and password2:
	        if password1 != password2:
	            raise forms.ValidationError(
	                self.error_messages['password_mismatch'],
	                code='password_mismatch',
	            )
	    return password2

	def save(self, commit=True):
	    self.user.set_password(self.cleaned_data['new_password1'])
	    if commit:
	        self.user.save()

	    return self.user
