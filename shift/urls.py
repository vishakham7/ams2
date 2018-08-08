from django.urls import path

from .views import( 
    	shiftAddView,
    	shiftListView,
    	shiftDeleteView,
    )

app_name = 'shift'
urlpatterns = [
	path('', shiftListView),
    path('add', shiftAddView),
    path('<int:id>/delete', shiftDeleteView),

]