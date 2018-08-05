"""amsystem URL Confipath('user/', include('user.urls')), 
    path('login/', include('login.urls')),
    path('attendance/', include('attendance.urls')),
    path('shift/', include('shift.urls')), 
    path('leaves/', include('leaves.urls')),
    path('calender/', include('calender.urls')),guration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# from login.views import test

from user.views import userDashboardView

from login.views import login

urlpatterns = [

	# path('', home_view, name='home'),
    path('admin/', admin.site.urls), 
    # path('user/', include('user.urls')), 
    path('login/', include('login.urls')),

    path('dashboard/', userDashboardView),
    path('user/', include('user.urls')), 
    path('login/', login),
    # path('user/', include('user.urls')), 
    # path('login/', include('login.urls')),
    # path('attendance/', include('attendance.urls')),
    # path('shift/', include('shift.urls')), 
    # path('leaves/', include('leaves.urls')),
    # path('calender/', include('calender.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
