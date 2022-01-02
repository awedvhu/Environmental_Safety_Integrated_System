"""Environmental_Safety_Integrated_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from myapp import views
from myapp.views import *
from django.urls import path


router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'department', views.DepartmentViewSet)
router.register(r'auth', views.AuthViewSet)
router.register(r'identify', views.IdentifyViewSet)
router.register(r'eventName', views.EventNameViewSet)
router.register(r'building', views.BuildingViewSet)
router.register(r'room', views.RoomViewSet)
router.register(r'level', views.LevelViewSet)
router.register(r'device', views.DeviceViewSet)
router.register(r'deviceFeature', views.DeviceFeatureViewSet)
router.register(r'yearlyDutyList', views.YearlyDutyListViewSet)
router.register(r'monthlyDutyList', views.MonthlyDutyListViewSet)
router.register(r'daylyDutyList', views.DaylyDutyListViewSet)
router.register(r'yearlyTotalEvent', views.YearlyTotalEventViewSet)
router.register(r'monthlyTotalEvent', views.MonthlyTotalEventViewSet)
router.register(r'daylyTotalEvent', views.DaylyTotalEventViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'dutyList', views.DutyListViewSet)
router.register(r'eventPIC', views.EventPICViewSet)

urlpatterns = [
    url('situation/', situation),
    url('pendingevent/', pendingevent),
    url('eventanalysis/', eventanalysis),
    url('historicalevent/', historicalevent),
    url('userset/', userset),
    url('levelset/', levelset),
    url('admin/', admin.site.urls),
    url('api/', include(router.urls)),
    url('', homepage),
]
