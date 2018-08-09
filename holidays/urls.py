from django.urls import path

from .views import( 
    	holidayAddView,
    	holidayListView,
    	holidayDeleteView,
    	calenderDetailView,
    )

app_name = 'holidays'
urlpatterns = [
	path('', holidayListView),
    path('add', holidayAddView),
    path('<int:id>/delete', holidayDeleteView),
    path('calender', calenderDetailView),

]