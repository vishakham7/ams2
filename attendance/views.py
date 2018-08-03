from django.shortcuts import render

# Create your views here.
def userAttendanceDetailView(request):
	return render(request, "test.html", {})
