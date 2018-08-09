from django.shortcuts import render, redirect, reverse

from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
# Create your views here.
from django.db import connection
from django.contrib import messages
from importlib import import_module
from django.conf import settings
from .form import LoginForm, ForgetPassForm, ResetPasswordForm
from masterApp.models import User

from django.utils import timezone

from django.contrib.sessions.backends.base import SessionBase
from django.contrib.sessions.models import Session
cursor = connection.cursor()
def UserLoginView(request):
	session_id = request.session.session_key
	if not session_id=="":
		if SessionBase.TEST_COOKIE_NAME not in request.session:
			[s.delete() for s in Session.objects.all() if s.get_decoded().get('_auth_user_hash') == user.get_session_auth_hash()]
			del request.session[session_id]

	my_form = LoginForm()
	if request.method == "POST":
		my_form = LoginForm(request.POST)
		if my_form.is_valid():
			email = request.POST.get('email')
			password = request.POST.get('password')
			cursor.execute('select email,password from masterApp_user where email = %s', [email])
			# if (User.objects.filter(email=email).exists() and User.objects.filter(password=password).exists()):
			# 	user = authenticate(email = email, password = password)
			row = cursor.fetchone()
			if(row[0]==email and row[1]==password):
				# print(email, password)
				# login(request, user)
				# Session.objects.filter(usersession__user=user).delete()

				# request.session.save()
				request.session['email'] = email
				session_id = request.session.session_key
				SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
				session_data = SessionStore().decode(session_id)
				# return HttpResponseRedirect('/dashboard')	
			else:
				return HttpResponseRedirect('')

		else:

			my_context = {
			"form" : my_form,
			}
			return render(request, "login.html", my_context)
		
	else:
		
		my_context = {

			"form" : my_form,
			"state" : "hey",
		}
		return render(request, "login.html", my_context)

	
    # return login(request)

# def UserLogoutView(request):
# 	if request.method=="POST":
# 		logout(request)
# 		session.pop('logged_in', None)
# 		return HttpResponseRedirect(reverse(''))
# 		my_context ={	
# 			"form" : my_form
# 		}
# 		return render(request, "login.html", my_context)



def UserLogoutView(request):
	for sesskey in request.session.keys():
		del request.session[sesskey]

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

				messages.success(request, 'password updated successfully!.')
				return HttpResponseRedirect('./')
			else:
				# del request.session['email']
				messages.error(request, 'password unmatch')
				# return HttpResponseRedirect('password_reset')
				return HttpResponseRedirect('./reset')

	else:
		my_content = {
			"form" : my_form
		}
		return render(request, "password_reset.html", my_content)
