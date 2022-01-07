from django.shortcuts import render
from myapp.serializers import *
from rest_framework import viewsets
from datetime import datetime
from django.http import JsonResponse
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class AuthViewSet(viewsets.ModelViewSet):
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class IdentifyViewSet(viewsets.ModelViewSet):
    queryset = Identify.objects.all()
    serializer_class = IdentifySerializer


class EventNameViewSet(viewsets.ModelViewSet):
    queryset = EventName.objects.all()
    serializer_class = EventNameSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceFeatureViewSet(viewsets.ModelViewSet):
    queryset = DeviceFeature.objects.all()
    serializer_class = DeviceFeatureSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventPICViewSet(viewsets.ModelViewSet):
    queryset = EventPIC.objects.all()
    serializer_class = EventPICSerializer


class YearlyDutyListViewSet(viewsets.ModelViewSet):
    queryset = YearlyDutyList.objects.all()
    serializer_class = YearlyDutyListSerializer


class MonthlyDutyListViewSet(viewsets.ModelViewSet):
    queryset = MonthlyDutyList.objects.all()
    serializer_class = MonthlyDutyListSerializer


class DaylyDutyListViewSet(viewsets.ModelViewSet):
    queryset = DaylyDutyList.objects.all()
    serializer_class = DaylyDutyListSerializer


class DutyListViewSet(viewsets.ModelViewSet):
    queryset = DutyList.objects.all()
    serializer_class = DutyListSerializer


class YearlyTotalEventViewSet(viewsets.ModelViewSet):
    queryset = YearlyTotalEvent.objects.all()
    serializer_class = YearlyTotalEventSerializer


class MonthlyTotalEventViewSet(viewsets.ModelViewSet):
    queryset = MonthlyTotalEvent.objects.all()
    serializer_class = MonthlyTotalEventSerializer


class DaylyTotalEventViewSet(viewsets.ModelViewSet):
    queryset = DaylyTotalEvent.objects.all()
    serializer_class = DaylyTotalEventSerializer


# APIView
class EventAPIView(APIView):

    def get(self, request):
        self.as_view()
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)

    def put(self, request):
        self.as_view()
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetail(APIView):
    def get_object(self, event_id):
        self.as_view()
        try:
            return Event.objects.get(eventID=event_id)
        except Event.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, event_id):
        event = self.get_object(event_id)
        serializer = EventSerializer(event)
        return Response(serializer.data)


class DeviceAPIView(APIView):

    def get(self, request):
        self.as_view()
        device = Device.objects.all()
        serializer = DeviceSerializer(device, many=True)
        return Response(serializer.data)

    def put(self, request):
        self.as_view()
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceDetail(APIView):
    def get_object(self, device_id):
        self.as_view()
        try:
            return Device.objects.get(deviceID=device_id)
        except Device.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, device_id):
        device = self.get_object(device_id)
        serializer = EventSerializer(device)
        return Response(serializer.data)


# Create your views here.
def homepage(request):
    today = datetime.today()
    now = datetime.now().hour
    nowmin = datetime.now().min
    duty_lists = DutyList.objects.filter(day=today.day)
    events = Event.objects.all()
    users = User.objects.all()
    peoplecount = 0
    invadecount = 0
    allpeoplecount = 0
    allinvadecount = 0
    for event in events:
        if event.eventName.eventName == "超過人數":
            allpeoplecount += 1
        else:
            allinvadecount += 1
        if event.day.day == today.day:
            if event.eventName.eventName == "超過人數":
                peoplecount += 1
            else:
                invadecount += 1

    return render(request, "homePage.html", locals())


def situation(request):
    today = datetime.today()
    events = Event.objects.filter(day=today.day)
    duty_lists = DutyList.objects.filter(day=today.day)
    users = User.objects.all()

    return render(request, "situation.html", locals())


def pendingevent(request):
    today = datetime.today()
    events = Event.objects.filter(day=today.day)
    duty_lists = DutyList.objects.filter(day=today.day)

    return render(request, "pendingEvent.html", locals())


def eventanalysis(request):
    today = datetime.today()
    events = Event.objects.filter(day=today.day)
    duty_lists = DutyList.objects.filter(day=today.day)

    return render(request, "eventAnalysis.html", locals())


def historicalevent(request):
    today = datetime.today()
    events = Event.objects.all().order_by('-eventID')
    duty_lists = DutyList.objects.filter(day=today.day)

    return render(request, "historicalevent.html", locals())


def userset(request):
    today = datetime.today()
    events = Event.objects.all()
    duty_lists = DutyList.objects.filter(day=today.day)
    users = User.objects.all()

    return render(request, "userSet.html", locals())


def levelset(request):
    today = datetime.today()
    events = Event.objects.all()
    duty_lists = DutyList.objects.filter(day=today.day)
    levels = Level.objects.all()

    return render(request, "levelSet.html", locals())


def deviceset(request):
    today = datetime.today()
    events = Event.objects.all()
    duty_lists = DutyList.objects.filter(day=today.day)
    devices = Device.objects.all()

    return render(request, "deviceSet.html", locals())
