from django.shortcuts import render
from masterApp.models import Holidays
import calendar
# Create your views here.

def calenderView(request):
	holiday_set = Holidays.objects.filter().order_by('date')

	days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
	
	context = {
		'holiday_list' : holiday_set,
		'no_of_days'   : {'jan':31, 'feb':28, 'mar':31, 'apr':30, 'may':31, 'jun':30, 'jul':31, 'aug':31, 'sep':30, 'oct':31, 'nov':30, 'dec':31},
		'month_names' : ['January','February','March','April','May','June','July','August','September','October','November','December'],
		'month_names_short' : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
		'week_names'	: ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
		'week_names_short'	: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
		'table_name'  : "Holidays Table",
	}
	return render(request, "calender/calender_detail.html", context)

def calenderDetailView(request, m_num):
	holiday_set = Holidays.objects.filter().order_by('date')

	days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
	# month_name_short = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
	month_names = ('January','February','March','April','May','June','July','August','September','October','November','December')
	days = days_in_month[m_num]
	first_week_day = calendar.weekday(2018, m_num+1, 1)
	dates = []
	for i in range(days):
		dates.append(i)
	print (dates)	
	blk=[]
	for i in range(35):
		blk.append(i)
	print(type(blk[6]))

	context = {
		'holiday_list' : holiday_set,
		'no_of_days' : days,
		'mon_no'  : m_num,
		'dates' : dates,
		'blocks' :blk,
		'first_week_day' : first_week_day,
		'month_name' : month_names[m_num],
		'year'		: 2018,
		# 'no_of_days'   : {'jan':31, 'feb':28, 'mar':31, 'apr':30, 'may':31, 'jun':30, 'jul':31, 'aug':31, 'sep':30, 'oct':31, 'nov':30, 'dec':31},
		'month_names' : ['January','February','March','April','May','June','July','August','September','October','November','December'],
		'month_names_short' : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
		'week_names'	: ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
		'week_names_short'	: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
		'table_name'  : "Holidays Table",
	}
	return render(request, "calender/calender_detail.html", context)

