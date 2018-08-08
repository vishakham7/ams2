from django.shortcuts import render, get_object_or_404

from .forms import CreateHolidayForm

from masterApp.models import Holidays

# Create your views here.


def holidayAddView(request):
	create_form = CreateHolidayForm(request.POST or None)
	user_set = Holidays.objects.all()
	context = {}
	if create_form.is_valid():
		print(create_form.cleaned_data)
		Holidays.objects.create(**create_form.cleaned_data)
		holiday_set = Holidays.objects.filter().order_by('date')
		context ={
			'holiday_list' 	: holiday_set,
			'table_name'  : "Holidays Table",
		}
	else:
		context ={
			'form' : create_form,
			'table_name'  : "Holidays Table",
		}
	return render(request, "holidays/holidays_detail.html", context)

def holidayListView(request):
	holiday_set = Holidays.objects.filter().order_by('date')
	context = {
		'holiday_list' : holiday_set,
		'table_name'  : "Holidays Table",
	}
	return render(request, "holidays/holidays_detail.html", context)


def holidayDeleteView(request, id):
	obj = Holidays.objects.filter(id=id).delete()
	print(obj)
	holiday_set = Holidays.objects.filter().order_by('date')
	context = {
		'holiday_list' : holiday_set,
		'table_name'  : "Holidays Table",
	}

	return render(request, "holidays/holidays_detail.html", context)