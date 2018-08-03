from django.shortcuts import render

# Create your views here.
def UserLoginView(request):
	return render(request, "test.html", {})

def ForgetPasswordView(request):
	return render(request, "test.html", {})

def UserLogoutView(request):	
	return render(request, "test.html", {})	

def test(request):
	return render(request, "test.html", {})		


	