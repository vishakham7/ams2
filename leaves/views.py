from django.shortcuts import render

# Create your views here.

def assignLeaveView(request):
	return render(request, "test.html", {})
