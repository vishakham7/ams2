from django.shortcuts import render, get_object_or_404

from .forms import CreateShiftForm

from masterApp.models import Shift
# Create your views here.

# def shiftAddView(request):
# 	return render(request, "test.html", {})

# def shiftListView(request):
# 	return render(request, "test.html", {})
	
# def shiftDetailView(request):
# 	return render(request, "test.html", {})		

# def shiftUpdateView(request):
# 	return render(request, "test.html", {})

# def shiftDeleteView(request):
# 	return render(request, "test.html", {})

# def assignShiftView(request):
# 	return render(request, "test.html", {})		

def shiftAddView(request):
	create_form = CreateShiftForm(request.POST or None)
	shift_set = Shift.objects.all()
	context = {}
	if create_form.is_valid():
		print(create_form.cleaned_data)
		Shift.objects.create(**create_form.cleaned_data)
		shift_set = Shift.objects.all()
		context ={
			'shift_list' 	: shift_set,
			'table_name'  : "Shift Table",
		}
	else:
		context ={
			'form' : create_form,
			'table_name'  : "Shift Table",
		}
	return render(request, "shift/shift_detail.html", context)

def shiftListView(request):
	shift_set = Shift.objects.filter().order_by('title')
	context = {
		'shift_list' : shift_set,
		'table_name'  : "Shift Table",
	}
	return render(request, "shift/shift_detail.html", context)


def shiftDeleteView(request, id):
	obj = Shift.objects.filter(id=id).delete()
	print(obj)
	shift_set = Shift.objects.all()
	context = {
		'shift_list' : shift_set,
		'table_name'  : "Shift Table",
	}

	return render(request, "shift/shift_detail.html", context)