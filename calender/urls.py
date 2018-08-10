from django.urls import path

from .views import( 
    	calenderView,
    	calenderDetailView,
    )

app_name = 'calender'
urlpatterns = [
    path('', calenderView),
    path('<int:m_num>', calenderDetailView),

]