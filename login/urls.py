from django.urls import path

from .views import( 
    	UserLoginView,
    	ForgetPasswordView,
    	UserLogoutView,
    	test,
    	resetPassword
    )

app_name = 'login'
urlpatterns = [
	path('', UserLoginView),
	path('password_reset', ForgetPasswordView),
	path('reset', resetPassword),
	path('test', test),
	path('',UserLogoutView)
	
]