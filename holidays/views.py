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


def calenderDetailView(request):
	holiday_set = Holidays.objects.filter().order_by('date')
	context = {
		'holiday_list' : holiday_set,
		'no_of_days'   : {'jan':31, 'feb':28, 'mar':31, 'apr':30, 'may':31, 'jun':30, 'jul':31, 'aug':31, 'sep':30, 'oct':31, 'nov':30, 'dec':31},
		'month_names' : ['January','February','March','April','May','June','July','August','September','October','November','December'],
		'month_names_short' : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
		'week_list'	: ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],
		'table_name'  : "Holidays Table",
	}
	return render(request, "holidays/calender_detail.html", context)