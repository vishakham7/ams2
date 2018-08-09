from django.shortcuts import render, get_object_or_404
from masterApp.models import User, Shift, Team, PaidLeaves, UserType

from .forms import(
	CreateUserForm,
 	UpdateUserForm,
 )
from amsystem.settings import LOGIN_URL
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def userDashboardView(request):
	return render(request, "home.html", {})
	# return HttpResponseRedirect('/login?next=dashboard')
	# return HttpResponseRedirect('/dashboard')

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def userDashboardView(request):
	return render(request, "home.html", {})

def userAddView(request):
	create_form = CreateUserForm(request.POST or None)
	user_set = User.objects.filter(del_flag=1)
	shift_set = Shift.objects.all()
	team_set = 	Team.objects.all()
	utype_set = 	UserType.objects.all()
	paidLeaves_set = 	PaidLeaves.objects.all()	
	context = {}
	if create_form.is_valid():
		print(create_form.cleaned_data)
		User.objects.create(**create_form.cleaned_data)
		user_set = User.objects.filter(del_flag=1)
		context ={
			'user_list' 	: user_set,
			'team_list'		: team_set,
			'shift_list'	: shift_set,
			'table_name'  : "Employee Table",
		}
	else:
		context ={
			'form' : create_form,
			# 'user_list' 	: user_set,
			'team_list'		: team_set,
			'shift_list'	: shift_set,
			'utype_list'	: utype_set,
			'paidLeaves_list': paidLeaves_set,
			'table_name'  : "Employee Table",
		}
	return render(request, "user/user_detail.html", context)

def userListView(request):
	user_set = User.objects.filter(del_flag=1)
	shift_set = Shift.objects.all()
	team_set = 	Team.objects.all()	
	context = {
		'user_list' : user_set,
		'team_list'		: team_set,
		'shift_list'	: shift_set,
		'table_name'  : "Employee Table",
	}
	return render(request, "user/user_detail.html", context)

def userDetailView(request):
	return render(request, "test.html", {})	

def userUpdateView(request, id=None):
	object = get_object_or_404(User, id=id)
	# print(object)
	form = UpdateUserForm(request.POST or None, instance=object)
	if form.is_valid():
		object = form.save()
		object.save()
		user_set = User.objects.all()
		shift_set = Shift.objects.all()
		team_set = 	Team.objects.all()	
		context = {
			'user_list' : user_set,
			'team_list'		: team_set,
			'shift_list'	: shift_set,
			'table_name'  : "Employee Table",
		}

	else :
		user_set = User.objects.all() 
		shift_set = Shift.objects.all()
		team_set = 	Team.objects.all()
		utype_set = 	UserType.objects.all()
		paidLeaves_set = PaidLeaves.objects.all()		
		context = {
			'id'    : id,
			'e_form'  : form,
			'user'	: object,
			# 'user_list' : user_set,
			'team_list'		: team_set,
			'shift_list'	: shift_set,
			'utype_list'	: utype_set,
			'paidLeaves_list': paidLeaves_set,
			'table_name'  : "Employee Table",
		}	
		
	return render(request, "user/user_detail.html", context)	

def userDeleteView(request, id):
	obj = User.objects.filter(id=id).update(del_flag=0)
	print(obj)
	user_set = User.objects.filter(del_flag=1)
	shift_set = Shift.objects.all()
	team_set = 	Team.objects.all()	
	context = {
		'user_list' : user_set,
		'team_list'		: team_set,
		'shift_list'	: shift_set,
		'table_name'  : "Employee Table",
	}

	return render(request, "user/user_detail.html", context)