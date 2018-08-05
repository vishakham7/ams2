from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

<<<<<<< HEAD
from .form import LoginForm, ForgetPassForm
from masterApp.models import User

=======
>>>>>>> 57da75e612a49d235069623f447e5c5483187e68

def UserLoginView(request):
	my_form = LoginForm()
	if request.method == "POST":
		my_form = LoginForm(request.POST)
		if my_form.is_valid():
			userObj = my_form.cleaned_data
			email = userObj['email']
			password = userObj['password']
			user = authenticate(email=email, password=password)
			if user is not None:
				login(request, user)
				request.session['email'] = email
			# return render(request,"test.html",{"email":email})
			# return HttpResponse("<strong>You are logged in.</strong>")
			return redirect('../login/test')

	else:
		my_content={
			"form" : my_form 
		}
		return render(request, "login.html", my_content)


def ForgetPasswordView(request):
	my_form = ForgetPassForm()
	if request.method == "POST":
		my_form = ForgetPassForm(request.POST)
		if my_form.is_valid():
			userObj = my_form.cleaned_data
			email = userObj['email']
			password = userObj['password']

			if(User.objects.filter(email=email).exists()):
				user = authenticate(email=email)
				login(request, user)
				my_content1 = {
					"form" : my_form
				}
				return render(request, "validate_email.html",my_content1)
			else:
				raise forms.ValidationError()
	my_content = {
		"form" : my_form
	}
	return render(request, "validate_email.html", my_content)



def UserLogoutView(request):
	my_form = LoginForm()
	my_content={
			"form" : my_form 
		}
	try:
		del request.session['email']
		return render(request, "login.html",my_content)
	except:
   		# return HttpResponse("<strong>You are logged out.</strong>")	
   		return render(request, "login.html",my_content)
   		# return render(request, "login.html",my_content)
	



<<<<<<< HEAD
def test(request):	
	my_form = LoginForm()
	my_content={
			"form" : my_form 
		}
	return render(request, "test.html", my_content)

def resetPassword(request):
	my_form = ForgetPassForm()
	my_content = {
		"form" : my_form
	}
	return render(request, "password_reset.html", my_content)
=======
def UserLogoutView(request):	
	return render(request, "test.html", {})	
<<<<<<< HEAD
=======

>>>>>>> 31fba0eb6352e9fa2056b523436ca5a0466f6dce
>>>>>>> 57da75e612a49d235069623f447e5c5483187e68
