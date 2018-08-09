from django import forms
# from bootstrap_datepicker.widgets import DatePicker
# TIME_FORMAT = '%d.%m.%Y'
from datetime import date 

from masterApp.models import Holidays

class CreateHolidayForm(forms.Form):
	title 		= forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Holiday title", "style":""}))
	
	date = forms.DateField(
		widget=forms.widgets.DateInput(
			format='%Y-%m-%d', 
			
			attrs={
				"class":"form-control",
				"placeholder":"Date",
				"type":"date",
				"value":date.today()
				}
			),
			
		)