from django import forms

from masterApp.models import Shift
import time
from datetime import datetime

strg = "2017-07-20-10-30"

dt = datetime.strptime(strg, '%Y-%m-%d-%H-%M')
tme = dt.time()
  # 10:30:00
class CreateShiftForm(forms.Form):
	title = forms.CharField(
		label='', 
		widget=forms.TextInput(
			attrs={
			"class":"form-control", 
			"placeholder":"Shift title", 
			
			}
		)
	)

	start_time = forms.TimeField(
			widget=forms.TimeInput(
				format=('%H:%M:%S'),
				# input_formats=('%H:%M:%S'),
				attrs={
				"class":"form-control",
				"placeholder":"Start time",
				"type":"time",
				"value":tme

				}	
			)

	)

	# date = forms.DateField(
	# 	widget=forms.widgets.DateInput(
	# 		format='%Y-%m-%d', 
			
	# 		attrs={
	# 			"class":"form-control",
	# 			"placeholder":"Date",
	# 			"type":"date",
	# 			"value":date.today()
	# 			}
	# 		),
			
	# 	)
	# start_time = forms.TimeField(input_formats=['%I:%M %p'])
	

	# start_time = datetime.datetime.strptime('12:12:12', '%H:%M:%S').time()
	# start_time = forms.DateTimeField(
	# 	widget=forms.widgets.DateInput(
	# 		format="%m/%d/%y", 
			# attrs={
			# 	"class":"form-control",
			# 	"placeholder":"Start time"
			# 	}
			# )
	# 	)

	end_time = forms.CharField(widget=forms.widgets.TextInput(attrs={
				"class":"form-control",
				"placeholder":"End time",
				"type":"time",
				"value":tme
				}
			)
	)

	# end_time = forms.DateTimeField(
	# 	widget=forms.widgets.DateInput(
	# 		format="%m/%d/%y", 
	# 		attrs={
	# 			"class":"form-control",
	# 			"placeholder":"End time"
	# 			}
	# 		)
	# 	)
	