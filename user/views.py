from django.shortcuts import render

# Create your views here.
def userAddView(request):
	return render(request, "test.html", {})

def userListView(request):
	return render(request, "test.html", {})

def userDetailView(request):
	return render(request, "test.html", {})	

def userUpdateView(request):
	return render(request, "test.html", {})

def userDeleteView(request):
	return render(request, "test.html", {})

