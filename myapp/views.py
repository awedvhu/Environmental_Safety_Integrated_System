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

    def get_object(self, pk):
        event = get_object_or_404(Event, pk=pk)
        return event

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
def homepage(request):
    today = datetime.today()
    now = datetime.now().hour
    duty_lists = DutyList.objects.filter(day=today.day)
    events = Event.objects.filter(day=today.day)
    count = 0
    for event in events:
        if event.day.day == today.day:
            count += 1

    return render(request, "homePage.html", locals())


def situation(request):
    today = datetime.today()
    events = Event.objects.filter(day=today.day)
    duty_lists = DutyList.objects.filter(day=today.day)

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
    events = Event.objects.all()
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

