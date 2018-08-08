from django import forms
from bootstrap_datepicker.widgets import DatePicker


from masterApp.models import Holidays

class CreateHolidayForm(forms.Form):
	title 		= forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Holiday title", "style":""}))
	# date		= forms.DateField(label='', widget=forms.DateInput(attrs={"class":"form-control","placeholder":"Date"}))
	date = forms.DateField(
		widget=forms.widgets.DateInput(
			format="%m/%d/%y", 
			attrs={
				"class":"form-control",
				"placeholder":"Date"
				}
			)
		)

	