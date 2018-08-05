from django.shortcuts import render
from masterApp.models import User

from .forms import CreateUserForm

# Create your views here.
def userDashboardView(request):
	return render(request, "home.html", {})

def userAddView(request):
	create_form = CreateUserForm(request.POST or None)
	query_set = User.objects.all()
	context = {}
	if create_form.is_valid():
		print(create_form.cleaned_data)
		User.objects.create(**create_form.cleaned_data)
		query_set = User.objects.all()
		context ={
			'object_list' 	: query_set
		}
	else:		
		context ={
			'form' : create_form,
			'object_list' 	: query_set
		}
	return render(request, "user/user_detail.html", context)

def userListView(request):
	query_set = User.objects.filter()
	context = {
		'object_list' : query_set,
		'table_name'  : "Employee Table",
	}
	return render(request, "user/user_detail.html", context)

def userDetailView(request):
	return render(request, "test.html", {})	

def userUpdateView(request):
	return render(request, "test.html", {})

def userDeleteView(request):
	return render(request, "test.html", {})


def add_user_view(request):
	

	return render(request, "testuser/testuser_detail.html", context)
