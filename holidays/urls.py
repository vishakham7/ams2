from django.urls import path

from .views import( 
    	holidayAddView,
    	holidayListView,
    	holidayDeleteView,
    )

app_name = 'holidays'
urlpatterns = [
	path('', holidayListView),
    path('add', holidayAddView),
    path('<int:id>/delete', holidayDeleteView),

]