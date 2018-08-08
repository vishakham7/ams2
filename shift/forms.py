from django import forms

from masterApp.models import Shift

class CreateShiftForm(forms.Form):
	title = forms.CharField(
		label='', 
		widget=forms.TextInput(
			attrs={
			"class":"form-control", 
			"placeholder":"Shift title", 
			"style":""
			}
		)
	)

	start_time = forms.CharField(widget=forms.widgets.TextInput(attrs={
				"class":"form-control",
				"placeholder":"Start time"
				}
			)
	)

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
				"placeholder":"End time"
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
	