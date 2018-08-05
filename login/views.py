from django.shortcuts import render, redirect, reverse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

from .form import LoginForm, ForgetPassForm
from masterApp.models import User


def UserLoginView(request):
	my_form = LoginForm()
	if request.method == "POST":
		my_form = LoginForm(request.POST)
		email = request.POST['email']
		password = request.POST['password']
		
		if (User.objects.filter(email=email).exists() or User.objects.filter(password=password).exists()):
			user = authenticate(email = email, password = password)
			login(request, user)
			# return HttpResponse("success")
			request.session['email'] = email
			return HttpResponseRedirect('/dashboard')	
			# return HttpResponse("You're logged in.")
		else:
			return HttpResponse("invalid user")
	else:
		
		my_context = {
			"form" : my_form
		}
		return render(request, "login.html", my_context)



def UserLogoutView(request):
	for sesskey in request.session.keys():
		del request.session[sesskey]
		logout(request)
		return render(request, "test.html",{})
	
	


def ForgetPasswordView(request):
	my_form = ForgetPassForm()
	if request.method == "POST":
		my_form = ForgetPassForm(request.POST)
		
		email = request.POST.get('email')

		if(User.objects.filter(email=email).exists()):
			user = authenticate(email=email)
			# return HttpResponse("reset")
			my_content1 = {
				"form" : my_form
			}
			# return render(request, "password_reset.html",my_content1)
			return HttpResponseRedirect('reset')
		else:
			# raise forms.ValidationError("no user")
			return HttpResponse("no user")
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
		# my_form = ForgetPassForm(request.POST, user=request.user)
		# if my_form.is_valid():
		# 	my_form.save()
		pass

	else:
		my_content = {
			"form" : my_form
		}
		return render(request, "password_reset.html", my_content)
