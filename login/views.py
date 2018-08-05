from django.shortcuts import render, redirect, reverse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

from .form import LoginForm, ForgetPassForm
from masterApp.models import User

# login done
def UserLoginView(request):
	my_form = LoginForm()
	if request.method == "POST":
		my_form = LoginForm(request.POST)
		email = request.POST['email']
		password = request.POST['password']
		if (User.objects.filter(email=email).exists() and User.objects.filter(password=password).exists()):
			user = authenticate(email = email, password = password)
			login(request, user)
			
			# return HttpResponse("success")
			return HttpResponseRedirect('../dashboard')
		else:
			return HttpResponse("invalid user")
	else:	
		my_context = {
			"form" : my_form
		}
		return render(request, "login.html", my_context)



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
	


def ForgetPasswordView(request):
	my_form = ForgetPassForm()
	if request.method == "POST":
		my_form = ForgetPassForm(request.POST)
		if my_form.is_valid():
			email = request.POST['email']

			if(User.objects.filter(email=email).exists()):
				# user = authenticate(email=email)
				my_content1 = {
					"form" : my_form
				}
				return render(request, "password_reset.html",my_content1)
			else:
				raise forms.ValidationError("no user")
	else:
		my_content = {
			"form" : my_form
		}
		return render(request, "validate_email.html", my_content)




def test(request):	
	return render(request, "test.html", {})

def resetPassword(request):
	my_form = ForgetPassForm()
	if request.method == "POST":
		my_form = ForgetPassForm(request.POST)
		my_form.cleaned_data
		email = my_form.cleaned_data['email']
		password = request.POST['password']
		User.objects.get(email='email')
		User.password = password
		User.save()
		return HttpResponseRedirect('/dashboard')
		
	my_content = {
		"form" : my_form
	}
	return render(request, "password_reset.html", my_content)

def UserLogoutView(request):	
	return render(request, "test.html", {})	
