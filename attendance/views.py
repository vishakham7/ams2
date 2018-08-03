from django.shortcuts import render


def userAttendanceDetailView(request):
	return render(request, "test.html", {})
