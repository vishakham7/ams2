from django.shortcuts import render, redirect, reverse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
# Create your views here.

from .form import LoginForm, ForgetPassForm, ResetPasswordForm
from masterApp.models import User



def UserLoginView(request):
	my_form = LoginForm()
	if request.method == "POST":
		my_form = LoginForm(request.POST)
		if my_form.is_valid():
			email = request.POST.get('email')
			password = request.POST.get('password')
			
			if (User.objects.filter(email=email).exists() and User.objects.filter(password=password).exists()):
				user = authenticate(email = email, password = password)
				login(request, user)
				request.session['email'] = email
				return HttpResponseRedirect('/dashboard')	
			else:
				return HttpResponseRedirect('')

		else:
			# print(my_form.errors)
			
			my_context = {
			"form" : my_form
			}
			return render(request, "login.html", my_context)

		
	else:
		
		my_context = {
			"form" : my_form
		}
		return render(request, "login.html", my_context)



def UserLogoutView(request):
	logout(request)
	return HttpResponseRedirect('')	


def ForgetPasswordView(request):
	my_form = ForgetPassForm()
	if request.method == "POST":
		my_form = ForgetPassForm(request.POST)
		
		email = request.POST.get('email')
		if my_form.is_valid():
			if(User.objects.filter(email=email).exists()):
				user = authenticate(email=email)
				my_content1 = {
					"form" : my_form
				}
				request.session['email'] = email
				return HttpResponseRedirect('reset')
				
			else:
				return HttpResponse("no user")
		else:
			my_context = {
			"form" : my_form
			}
			return render(request, "validate_email.html", my_context)

	else:
		my_content = {
			"form" : my_form
		}
		return render(request, "validate_email.html", my_content)




def test(request):	
	return render(request, "test.html", {})

def resetPassword(request):
	my_form = ResetPasswordForm()
	if request.method == "POST":
		my_form = ResetPasswordForm(request.POST)
		new_password = request.POST.get('password')
		repeat_new_password = request.POST.get('password1')
		# print (new_password)
		email = request.session['email']
		if(User.objects.filter(email=email).exists()):
			user = authenticate(email=email)
			# User.password2 = new_password
			if new_password == repeat_new_password:
				u = User.objects.get(email=email)
				u.password = new_password
				u.save()

				return HttpResponseRedirect('./')
				messages.success(request, "Configuration successfully submitted")
			else:
				del request.session['email']
				return HttpResponseRedirect('password_reset')
		else:
			return HttpResponse("something went wrong")

	else:
		my_content = {
			"form" : my_form
		}
		return render(request, "password_reset.html", my_content)
