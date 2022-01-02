from rest_framework import serializers
from myapp.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = '__all__'


class IdentifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Identify
        fields = '__all__'


class EventNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventName
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class DeviceFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceFeature
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventPICSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPIC
        fields = '__all__'


class YearlyDutyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearlyDutyList
        fields = '__all__'


class MonthlyDutyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyDutyList
        fields = '__all__'


class DaylyDutyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaylyDutyList
        fields = '__all__'


class DutyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DutyList
        fields = '__all__'


class YearlyTotalEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearlyTotalEvent
        fields = '__all__'


class MonthlyTotalEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyTotalEvent
        fields = '__all__'


class DaylyTotalEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaylyTotalEvent
        fields = '__all__'
