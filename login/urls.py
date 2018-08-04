from django.urls import path

from .views import( 
    	login,
    	userListView,
    	userDetailView,
    	userUpdateView,
    	userDeleteView,
    )

app_name = 'user'
urlpatterns = [
	path('', userListView),
    path('<int:id>', userDetailView),
    path('add', userAddView),
    path('<int:id>/delete', userDeleteView),
    path('<int:id>/update', userUpdateView),

]